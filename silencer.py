#!/usr/bin/python3
try:
    print("""                     
                                                                          ,,,,      
                                                                      ,,,,,,,,,,    
                                                                   ,,,,,,,,,,,      
                                                               .,,,,,,,,,,,         
                                                            ,,,,,,,,,,,             
                                                         ,,,,,,,,,,,                
                                                     ,,,,,,,,,,,.                   
                                                   ,,,,,,,,,,                       
                                                    .,,,,,                          
                                           //   /                                   
                                        /////*                                      
                                    //////    .,,                                   
                                 //////    ,,,,.                                    
                             */////.    ,,,,                                        
                          //////    ,,,,,                                           
                      ,/////*    ,,,,                                               
                   //////    ,,,,,                                                  
                //////    ,,,,                                                      
            //////     ,,,,                                                         
         //////    ,,,,,,,                                                          
        ///.    ,,,,,,,,,,                                                          
            ,,,,,,,,,,,,,,,                                                         
          ,,,.  .,,,,,,,,,,                                                         
                   ,,,,,,,,,                                                        
                    ,,,,,,,,,                                                       
                    .,,,,,,,,,                                                      
                     ,,,,,,,,,                                                      
                      ,,,,,,,,,                                                     
                       ,,,,    
                       
        Version 1.1
        If you have any questions or would like to connect, feel free to contact me:
        
        
        
        Website: https://marcoliberale.com/
    
        Email: contact@marcoliberale.com
        
        Github: https://github.com/marco-liberale
        
        LinkedIn: https://www.linkedin.com/in/marco-liberale-98b706292/
    
        Twitter/X: https://twitter.com/marco_liberale
    
                                                         
      """)

    import subprocess
    import socket
    import os
    import sys
    import select
    import colorama
    from optparse import OptionParser
    import os

    if os.getuid() == 0:
        print('Running as root')
    else:
        print('Please run as root')
        exit(0)

    def is_package_installed(package_name):
        try:
            __import__(package_name)
            return True
        except ImportError:
            return False
    parser = OptionParser()
    parser.add_option("-n", "--new-ip", dest="newip", action="store_true", default=False,
                      help="Get a new TOR IP. This option does not require a value.")
    parser.add_option("-c", "--command", dest="cmd",
                      help="Specify the command to run. This option requires a value.")
    (options, args) = parser.parse_args()
    def check_rq():
        print("checking if tor is installed")
        if is_package_installed("tor"):
            print("Please install tor before using this tool")
            exit(1)
        print("Starting tor")
        subprocess.run(["sudo", "systemctl", "start", "tor"], check=True)
    check_rq()
    def check_internet():
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False


    def run_command_through_tor(command):
        tor_command = f'torsocks {command}'
        process = subprocess.Popen(tor_command, shell=True)
        output, error = process.communicate()

        if error:
            print(f'Error: {error}')

    def run_command(command):
        if check_internet():
            run_command_through_tor(command)
        else:
            print('No internet connection. Cannot run the command.')

      # Read from stdin
    if options.newip:
        print(colorama.Fore.YELLOW + "Getting a new TOR ip..." + colorama.Style.RESET_ALL)
        os.system("sudo service tor restart")
        print(colorama.Fore.GREEN + "Done" + colorama.Style.RESET_ALL)
    if options.cmd:

        run_command(options.cmd)
    else:
        if select.select([sys.stdin, ], [], [], 0.0)[0]:
            command = sys.stdin.read().strip()  # Read from stdin only if there is input
            run_command(command)
        else:
            print("No input provided.")
except Exception as e:
    print("Error: " + str(e))
    exit(1)
except KeyboardInterrupt:
    ex = input("Exit? (Y/N): ")
    if ex.lower() == "y":
        exit(0)
