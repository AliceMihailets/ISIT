ans = [0, 1]

class TreeNode:
    def __init__(self, value, rule=None, left=None, right=None, solution=None, parent=None, ruleValue=None):
        self.value = value
        self.left = left
        self.right = right
        self.rule = rule
        self.solution = solution
        self.parent = parent
        self.ruleValue = ruleValue


class Rule:
    def __init__(self, condition1, conditionvalue1, condition2, conditionvalue2, action):
        self.condition1 = condition1
        self.condition2 = condition2
        self.conditionvalue1 = conditionvalue1
        self.conditionvalue2 = conditionvalue2
        self.action = action

    def ReadTree(node, ruleValue):
        while node.left != None or node.right != None:
            print(node.rule.condition1)
            try:
                if (ans[int(input())]):
                    node.rule.conditionvalue1 = 1 - node.rule.conditionvalue1
                print(node.rule.condition2)
                if (ans[int(input())]):
                    node.rule.conditionvalue2 = 1 - node.rule.conditionvalue2
            except IndexError as ex:
                print("Что-то пошло не так( \nИспользуйте для ответа: 0-нет, 1-да")
                Rule.ReadTree(node, ruleValue)

                
            if node.rule.action == "sum":
                if node.rule.conditionvalue1 > node.rule.conditionvalue2:
                    node.ruleValue = node.rule.conditionvalue1
                else:
                    node.ruleValue = node.rule.conditionvalue2
            else:
                if node.rule.conditionvalue1 > node.rule.conditionvalue2:
                    node.ruleValue = node.rule.conditionvalue2
                else:
                    node.ruleValue = node.rule.conditionvalue1

            if node.ruleValue > 0.5:
                node.ruleValue = node.ruleValue + ruleValue * (1 - node.ruleValue)
                Rule.ReadTree(node.right, node.ruleValue)
            else:
                node.ruleValue = node.ruleValue + ruleValue * (1 - node.ruleValue)
                Rule.ReadTree(node.left, node.ruleValue)

        print(node.solution + "\n\n" + "Вероятность:" + str(ruleValue))


rule1 = Rule("Доход вашей семьи больше 50 т.р. в месяц?", 0.7, "В вашей семье больше 2 человек?", 0.6, "sum")
rule2 = Rule("Вы можете позволить себе периодическую покупку вещей?", 0.8, "А аксессуаров?", 0.9, "sum")
rule3 = Rule("Вы можете позволить себе питаться в ресторанах каждые выходные?", 0.9, "А в кафе?", 0.7, "sum")
rule4 = Rule("Вы можете позволить себе периодическую покупку бытовой техники?", 0.9, "Вы имеете какие-либо платные подписки?", 0.8, "sum")
rule5 = Rule("Вы можете позволить себе покупку автомобиля?", 0.7, "Вы можете периодически кататься на такси?", 0.6, "multiply")
rule6 = Rule("Имеете ли вы возможность ходить на концерты?", 0.7, "А в кино?", 0.9, "sum")

nodeSolution1 = TreeNode(5, None, None, None, "Вам стоит заняться планированием семейного бюджета")
nodeSolution2 = TreeNode(5, None, None, None, "Вы можете не особо планировать семейный бюджет")
nodeSolution3 = TreeNode(5, None, None, None, "Вам стоит ОЧЕНЬ тщательно планировать семейный бюджет или найти другую работу")
nodeSolution4 = TreeNode(5, None, None, None, "У вас столько денег, что вы можете забыть о планировании бюджета")
nodeSolution5 = TreeNode(5, None, None, None, "У вас достаточно денег, но вы можете уделять немного времени планированию бюджета")
nodeSolution6 = TreeNode(5, None, None, None, "Вам стоит раз в год заниматься планированием семейного бюджета")
nodeSolution7 = TreeNode(5, None, None, None, "Вам стоит раз в месяц заниматься планированием семейного бюджета")

node6 = TreeNode(5, rule6, nodeSolution6, nodeSolution7)
node5 = TreeNode(5, rule5, nodeSolution4, nodeSolution5)
node4 = TreeNode(5, rule4, node5, node6)
node3 = TreeNode(5, rule3, nodeSolution2, nodeSolution3)
node2 = TreeNode(5, rule2, node4, nodeSolution1)
node1 = TreeNode(5, rule1, node2, node3)

Rule.ReadTree(node1, 0)

