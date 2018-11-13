import paramiko

class sa(object):
    def __init__(self):
        self.ssh = None
    
    def connect(self, args):
        try:
            #self.ssh = paramiko.SSHClient()
            #self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #self.ssh.connect(hostname=args['name'], username=args['user'], password=args['password'])
            self.ssh = 'done' # comment this line while executing
        except:
            raise Exception("connection failed")
        
    def create_alias(self, args):
        if self.ssh:
            cmds = []
            for alias in args['aliases'].items():
                print alias
                cmd = 'alicreate \"'+'\",\"'.join(alias)+'\"'
                cmds.append(cmd)
            try:
                #self.exec_command(';'.join(cmds))
                print ";".join(cmds)
            except:
                raise Exception("failed to execute the command"+";".join(cmds))
        else:
            raise Exception("connection has not been established")
    def verify_alias(self, args):
        if self.ssh:
            
            cmds = ( "alishow "+x for x in args['aliases'] )
            #(stdin, stdout, stderr) = self.ssh.exec_command(";",join(cmds))
            print ";".join(cmds)
            #if len(stdout.readlines()) != (len(keys)*2):
            #    raise Exception("failed create complete aliasis")
    def disconnect(self):
        #self.ssh.close()
        pass
