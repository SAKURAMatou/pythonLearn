from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_headers

router = APIRouter(prefix="/items",
                   tags=['items'],
                   dependencies=[Depends(get_token_headers)],
                   responses={404: {"description": "Not found"}})

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


# router中已经定义了tag以及response，在对应的具体的接口路径中再次定义则会起到添加的效果
# 最后的这个路径操作将包含标签的组合：["items"，"custom"]
# 并且在文档中也会有两个响应，一个用于 404，一个用于 403
@router.put("/item_id", tags=["custom"], responses={403: {"description": "Operation forbidden"}})
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
