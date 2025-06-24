from supabase import create_client
from .config import SUPABASE_URL, SUPABASE_KEY

sb = create_client(SUPABASE_URL, SUPABASE_KEY)

async def list_pending_orders():
    return sb.table("orders").select("*").eq("status", "pending").execute().data

async def take_order(order_id, master_id):
    # добавить в order_progress + обновить статус
    sb.table("order_progress").insert({
      "order_id": order_id,
      "master_id": master_id,
      "status": "in_progress"
    }).execute()
    sb.table("orders").update({"status":"in_progress"}).eq("id",order_id).execute()

async def cancel_order(order_id, master_id, comment):
    sb.table("order_progress").insert({
      "order_id": order_id,
      "master_id": master_id,
      "status": "not",
      "comment": comment
    }).execute()
    sb.table("orders").update({"status":"not"}).eq("id",order_id).execute()
