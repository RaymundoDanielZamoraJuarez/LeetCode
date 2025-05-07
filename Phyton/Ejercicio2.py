"""
LRU Cache:

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

"""
# Se crea la clase "Node", en la cual se guarda un par (key, value)
# prev y next son punteros
# Dado un nodo, nos permiten sacar o insertar en cualquier posción O(1)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# capacity: pares MÁX que se pueden almacenar
# cache: dict que dado un key se devuelve al nodo asociado
# head/tail: nodos sentinela, uno detrás de otro
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # clave -> nodo

        # Creamos nodos fantasma para head y tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Elimina nodo de la lista
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        # Inserta el nodo justo después de head (al frente)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node) # Se saca donde esté
            self._add_to_front(node) # Se mete al frente
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key]) # Si ya existía, se borra

        node = Node(key, value)
        self.cache[key] = node # Actualiza/Agrega en el dict
        self._add_to_front(node) # Agrega al frente

        if len(self.cache) > self.capacity:
            # Eliminar el nodo menos recientemente usado
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

#Ejemplo dado en el INPUT del problema: 

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # 1
    lru.put(3, 3)
    print(lru.get(2))  # -1
    lru.put(4, 4)
    print(lru.get(1))  # -1
    print(lru.get(3))  # 3
    print(lru.get(4))  # 4