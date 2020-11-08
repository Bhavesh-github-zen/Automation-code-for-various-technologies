import os
import getpass
os.system("tput setaf 11")
print("################################################### WELCOME ###################################################")
while(1):
		os.system("tput setaf 11")
		j=input("""
1. For Docker
2. For hadoop 
3. For partition
4. For Webserver
5. To exit

Enter your choice: """)
		if(j=="1"):
			os.system("tput setaf 85")
			k=input("""
1. To install docker-ce
2. To start/stop docker service
3. To Show containers
4. To download image
5. To start, stop,launch, remove and attach the Container
6. To exit

Enter your choice: """)
			if(k=="1"):
				os.system("yum install docker-ce")
			if(k=="2"):
				l=input("""
1. For temporarily start the docker service
2. For permannently start the docker service
3. To temporarily stop the docker service
4. To permanently stop the docker service

Enter your choice: """)
				if(l=="1"):
					os.system("systemctl start docker")
				if(l=="2"):
					os.system("systemctl enable docker")
				if(l=="3"):
					os.system("systemctl stop docker")
				if(l=="4"):
					os.system("systemctl disable docker")
			if(k=="3"):
				p=input("""
1. To show only running containers
2. To show all containers

Enter your choice: """)
				if(p=="1"):
					os.system("docker ps")
				if(p=="2"):
					os.system("docker ps -a")
			if(k=="4"):
				a=input("\nEnter Docker OS name :")
				b=input("Enter it's version :")
				os.system("docker pull {}:{}".format(a,b))
			if(k=="5"):
				o=input("""
1. To start the container
2. To stop the container
3. To attach the container
4. To launch the  container
5. To remove the container

Enter your choice: """)
				if(o=="1"):
					y=input("\nEnter the name or id of container :")
					os.system("docker start {}".format(y))
				if(o=="2"):
					y=input("\nEnter the name or id of container :")
					os.system("docker stop {}".format(y))
				if(o=="3"):
					y=input("\nEnter the name or id of container :")
					os.system("docker attach {}".format(y))
				if(o=="4"):
					t=input("""
1. To launch container by giving it name
2. To launch container without giving it's name

Enter your choice: """)
					if(t=="1"):
						d=input("\nEnter the name that you wanted to give to your container")
						e=input("Enter the OS name")
						f=input("Enter the OS version")
						os.system("docker run -it --name {} {}:{}".format(d,e,f))
					if(t=="2"):
						e=input("\nEnter the OS name")
						f=input("Enter the OS version")
						os.system("docker run -it {}:{}".format(e,f))

				if(o=="5"):
					y=input("\nEnter the name or id of container :")
					os.system("docker rm {}".format(y))
			if(k=="6"):
				continue
		if(j=="2"):
			os.system("tput setaf 75")
			x=input("""
What do you want to configure in hadoop ?
1. Master
2. Slave
3. Client
4. For Exit

Enter your choice : """)
			if(x=="1"):
				print("""*************** Master Configuration ***************
Now edit the hdfs-site.xml file""")
				os.system("sleep 2")
				os.system("vim  /etc/hadoop/hdfs-site.xml")
				print("Now edit the core-site.xml file")
				os.system("sleep 2")
				os.system("vim  /etc/hadoop/core-site.xml")
				os.system("hadoop namenode -format")
				os.system("hadoop-daemon.sh start namenode")
				os.system("sleep 2")
				os.system("jps")
				print("Master configured successfully")
			if(x=="2"):
				print("""*************** Slave Configuration ***************
Now edit the hdfs-site.xml file""")
				os.system("sleep 2")
				os.system("vim  /etc/hadoop/hdfs-site.xml")
				print("Now edit the core-site.xml file")
				os.system("sleep 2")
				os.system("vim  /etc/hadoop/core-site.xml")
				os.system("hadoop-daemon.sh start datanode")
				os.system("sleep 2")
				os.system("jps")
				print("Slave configured successfully")
			if(x=="3"):
				print("""*************** Client Configuration ***************
Now edit the hdfs-site.xml file""")
				os.system("sleep 2")
				os.system("vim  /etc/hadoop/hdfs-site.xml")
				print("Now edit the core-site.xml file")
				os.system("sleep 2")
				os.system("vim  /etc/hadoop/core-site.xml")
				print("Client configured successfully")
			if(x=="4"):
				continue
		if(j=="3"):
			os.system("tput setaf 120")
			q=input("""
1. For creating partition
2. For formatting the Partition
3. For mounting of partition
4. For unmounting of partition
5. Exit

Enter your choice : """)
			if(q=="1"):
				pa=input("Enter the harddisk name or path for creating it's partition : ")
				os.system("fdisk {}".format(pa))
				os.system("partprobe {}".format(pa))
				os.system("udevadm settle")
				print("Partition created successfully")
			if(q=="2"):
				fo=input("Enter the partition name or path for formatting : ")
				os.system("mkfs.ext4 {}".format(fo))
				print("Formatting of partition {} is done".format(fo))
			if(q=="3"):
				mo=input("Enter the partition name or path for mounting : ")
				fol=input("Enter the folder name for mounting : ")
				os.system("mount {} {}".format(mo,fol))
				print("Mounted Successfully")
			if(q=="4"):
				umo=input("Enter the partition name or path for unmounting : ")
				ufol=input("Enter the folder name for unmounting : ")
				os.system("umount {} {}".format(umo,ufol))
				print("Unmounted successfully")
			if(q=="5"):
				continue
		if(j=="4"):
			os.system("tput setaf 135")
			s=input("""
1. For configuring webserver
2. For making webpages
3. To exit

Enter your choice : """)
			if(s=="1"):
				os.system("dnf install httpd")
				r=input("\nMake your webpage, enter the name of webpage in .html format :- ")
				os.system("vim /var/www/html/{}".format(r))
				os.system("cd")
				print("Webpage created successfully ")
				os.system("systemctl start httpd")
				print("Webserver configured successfully ")
			if(s=="2"):
				os.system("cd /var/www/html")
				r=input("\nMake your webpage, enter the name of webpage in .html format :- ")
				os.system("vim /var/www/html/{}".format(r))
				os.system("cd")
				print("Webpage created successfully ")
				os.system("cd")
			if(s=="3"):
				continue	
		if(j=="5"):
			exit()
