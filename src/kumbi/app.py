from kumbi.services.task_services import dispatcher
from kumbi.user_interface.cli_config import get_cli_input

def main():
    dispatcher(get_cli_input())
    

if __name__ == "__main__":
    main()