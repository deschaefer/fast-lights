import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from view_models.account.account_view_model import AccountViewModel
from view_models.account.login_view_model import LoginViewModel
from view_models.account.register_view_model import RegisterViewModel

router = fastapi.APIRouter()


@router.get('/account')
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout(request: Request):
    return {}
