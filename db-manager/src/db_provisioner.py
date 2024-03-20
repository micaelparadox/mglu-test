class DBProvisioner:
    @staticmethod
    def provision(flavor, storage):
        print(f"Provisionando DB com tipo {flavor} e armazenamento de {storage}GB")
        docker_image = DBProvisioner.get_docker_image(flavor)
        vm_ip = DBProvisioner.provision_vm_with_compute_xaas(flavor, storage)
        DBProvisioner.start_postgres_container(vm_ip, docker_image)
        return {
            "message": f"DB provisionado com tipo {flavor} e armazenamento {storage}GB",
            "flavor": flavor,
            "storage": storage,
            "vm_ip": vm_ip
        }

    @staticmethod
    def get_docker_image(flavor):
        return f"mydbaaS/postgres-{flavor}:latest"

    @staticmethod
    def provision_vm_with_compute_xaas(flavor, storage):
        return "192.168.1.100"

    @staticmethod
    def start_postgres_container(vm_ip, docker_image):
        print(f"Iniciando o container {docker_image} na VM {vm_ip}")
