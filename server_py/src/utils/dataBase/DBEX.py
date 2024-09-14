from fastapi import APIRouter, HTTPException, Request, status
class DBEX:
    def controller_init(routerThis,description,DoService, Do, DoCreate ) -> str:
        @routerThis.post(
            "/default_add",
            status_code=status.HTTP_201_CREATED,
            summary=f"添加{description}返回id",
        )
        async def add(do: DoCreate) -> str:
            return await DoService.add(do)