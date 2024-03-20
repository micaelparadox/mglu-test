resource "aws_instance" "db_vm" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "DB VM"
  }

  volume_tags = {
    Name = "DB Data Volume"
  }

  ebs_block_device {
    device_name = "/dev/sdh"
    volume_size = var.volume_size
    volume_type = "gp2"
  }

  vpc_security_group_ids = [aws_security_group.db_sg.id]
}

resource "aws_security_group" "db_sg" {
  name        = "db_sg"
  description = "Permitir tráfego do PostgreSQL"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

variable "volume_size" {
  description = "Tamanho do volume para os dados do banco de dados em GB"
  default     = 100
}

variable "key_name" {
  description = "Nome da chave SSH a ser anexada à instância"
}

variable "vpc_id" {
  description = "ID da VPC onde o grupo de segurança será criado"
}
