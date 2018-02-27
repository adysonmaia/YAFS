"""
    This algorithm have one obligatory functions:

        *get_path*: It provides the route to follow the message within the topology to reach the destination module, it can also be seen as an orchestration algorithm.


"""
import random
import logging

import networkx as nx


class Selection(object):
    """
    A selection algorithm provide the route among topology entities for that a message reach the destiny module.

    .. note:: A class interface
    """

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.transmit = 0.0
        self.lat_acc = 0.0
        self.propagation = 0.0

    def get_path(self, sim, app_name, message, topology_src,alloc_DES, alloc_module, traffic):
        """
        Args:

            sim (yafs.core.Sim)

            src (int): the node source

            dst (dst): the node destiny

            message (yafs.application.Message)

            traffic (dict): the current occupation of the network

        Returns:

            a path among nodes

        .. attention:: override required

        """
        self.logger.debug("Selection")
        """ Define Selection """
        path = []
        ids = []

        """ END Selection """
        return path,ids

class OneRandomPath(Selection):
    """
    Among all the possible options, it returns a random path.
    """

    def get_path(self, sim, app_name, message, topology_src,alloc_DES, alloc_module, traffic):
        paths = []
        dst_idDES = []
        src_node = topology_src
        DES = alloc_module[message.app_name][message.dst]
        for idDES in DES:
            dst_node = alloc_module[idDES]
            pathX = list(nx.all_simple_paths(sim.topology.G, source=src_node, target=dst_node))
            one = random.randint(0, len(pathX) - 1)
            paths.append(pathX[one])
            dst_idDES.append(idDES)
        return paths,dst_idDES



class First_ShortestPath(Selection):
    """Among all possible shorter paths, returns the first."""

    def get_path(self, sim, app_name,message, topology_src, alloc_DES, alloc_module, traffic):
        paths = []
        dst_idDES = []

        node_src = topology_src #TOPOLOGY SOURCE where the message is generated
        DES_dst = alloc_module[app_name][message.dst]

        #Among all possible path we choose the smallest
        bestPath = []
        bestDES = []
        for des in DES_dst:
            dst_node = alloc_DES[des]
            # print "DES Node %i " %dst_node
            path = list(nx.shortest_path(sim.topology.G, source=node_src, target=str(dst_node)))
            bestPath = [path]
            bestDES  = [des]


        return bestPath,bestDES
