import random


class NodeDistributor:

    distributStep = 0
    nodeDistributors = []
    isResevedTask = False

    nodeUsed = {}
    iteration = 0

    @staticmethod
    def stat_Ini(ds, nd):
        NodeDistributor.distributStep=ds
        NodeDistributor.nodeDistributors=nd

    @staticmethod
    def clear():
        NodeDistributor.nodeUsed = {}
        NodeDistributor.iteration = 0

    def runAction(self):
        NodeDistributor.nodeUsed[self]=1
        for id in range(NodeDistributor.distributStep):
            NodeDistributor.iteration += 1
            node = random.randint(0, len(NodeDistributor.nodeDistributors)-1)
            nodeDistributor = NodeDistributor.nodeDistributors[node]
            if NodeDistributor.nodeUsed.get(nodeDistributor, 0) != 1:
                nodeDistributor.runAction()


def test(step: int, length: int):
    nodeDistributors = []; effect = 0.0; tokens=1000;
    for i in range(length):
        nodeDistributors.append(NodeDistributor())
    NodeDistributor.stat_Ini(step, nodeDistributors)
    for id in range(tokens):
        nodeDistributors[0].runAction()
        res_node = len(NodeDistributor.nodeUsed); tot_node=len(NodeDistributor.nodeDistributors)
        effect += (res_node / tot_node) * 100
        print('total iterations='+str(NodeDistributor.iteration)+
              ' total reseved nodes='+str(res_node)+
              ' total nodes='+  str(tot_node))

        NodeDistributor.clear();
    effect /= tokens
    print('In '+str((round(effect*1000))/1000)+' cases all nodes received the packet')


if __name__ == '__main__':
    infect_steps = int(input('Input infected step = '))
    length = int(input('Input total nodes = '))
    test(infect_steps, length)

