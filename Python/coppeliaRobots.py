import sim
import numpy as np
def simConnect(port):
        sim.simxFinish(-1) # just in case, close all opened connections
        clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) # Conectarse
        if clientID == 0: print("[+] Conectado al puerto", port)
        else: print("[-] Error -  No se pudo establecer conexión con el simulador ")
        return clientID

class plannarRobot:
    def __init__(self):
        self.clientID = 0
        self.joint_1_ID = 0
        self.joint_2_ID = 0
        self.joint_3_ID = 0
        self.dummy_ID = 0
        self.returnCode = 0

    def robotInit(self, clientID):
        self.clientID = clientID
        try:
            self.returnCode, self.joint_1_ID =  sim.simxGetObjectHandle(self.clientID,'Joint_01',sim.simx_opmode_blocking)
            self.returnCode, self.joint_2_ID =  sim.simxGetObjectHandle(self.clientID,'Joint_3',sim.simx_opmode_blocking)
            self.returnCode, self.joint_3_ID =  sim.simxGetObjectHandle(self.clientID,'Joint_03',sim.simx_opmode_blocking)
            self.returnCode, self.dummy_ID =  sim.simxGetObjectHandle(self.clientID,'dummy',sim.simx_opmode_blocking)
            print(self.joint_1_ID)
            print(self.joint_2_ID)
            print(self.joint_3_ID)
            print(self.dummy_ID)
        except:
            print("[-] ERROR - no se encontró componentes del robot")
    def getDummyPosition(self):
        self.returnCode, dummyPosition = sim.simxGetObjectPosition(self.clientID, self.dummy_ID, -1, sim.simx_opmode_blocking)
        return dummyPosition
    def moveRobot(self, phi1, phi2, phi3):
        phi1 = phi1*np.pi/180.0
        phi2 = phi2*np.pi/180.0
        phi3 = phi3*np.pi/180.0
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_1_ID, phi1, sim.simx_opmode_streaming)
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_2_ID, phi2, sim.simx_opmode_streaming)
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_3_ID, phi3, sim.simx_opmode_streaming)
        
        
class simple3GDM:
    def __init__(self):
        self.clientID = 0
        self.joint_1_ID = 0
        self.joint_2_ID = 0
        self.joint_3_ID = 0
        self.dummy_ID = 0
        self.returnCode = 0

    def robotInit(self, clientID):
        self.clientID = clientID
        try:
            self.returnCode, self.joint_1_ID =  sim.simxGetObjectHandle(self.clientID,'Joint_01',sim.simx_opmode_blocking)
            self.returnCode, self.joint_2_ID =  sim.simxGetObjectHandle(self.clientID,'Joint_3',sim.simx_opmode_blocking)
            self.returnCode, self.joint_3_ID =  sim.simxGetObjectHandle(self.clientID,'Joint_03',sim.simx_opmode_blocking)
            self.returnCode, self.dummy_ID =  sim.simxGetObjectHandle(self.clientID,'dummy',sim.simx_opmode_blocking)
            print(self.joint_1_ID)
            print(self.joint_2_ID)
            print(self.joint_3_ID)
            print(self.dummy_ID)
        except:
            print("[-] ERROR - no se encontró componentes del robot")
    def getDummyPosition(self):
        self.returnCode, dummyPosition = sim.simxGetObjectPosition(self.clientID, self.dummy_ID, -1, sim.simx_opmode_blocking)
        return dummyPosition
    def move(self, phi1, phi2, phi3):
        phi1 = phi1*np.pi/180.0
        phi2 = phi2*np.pi/180.0
        phi3 = phi3*np.pi/180.0
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_1_ID, phi1, sim.simx_opmode_streaming)
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_2_ID, phi2, sim.simx_opmode_streaming)
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_3_ID, phi3, sim.simx_opmode_streaming)
    def moveBase(self, phi):
        phi = phi*np.pi/180.0
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_1_ID, phi, sim.simx_opmode_streaming)
    def moveJoin01(self, phi):
        phi = phi*np.pi/180.0
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_2_ID, phi, sim.simx_opmode_streaming)
    def moveJoin02(self, phi):
        phi = phi*np.pi/180.0
        self.returnCode = sim.simxSetJointTargetPosition (self.clientID, self.joint_3_ID, phi, sim.simx_opmode_streaming)
        

    
    
    


    