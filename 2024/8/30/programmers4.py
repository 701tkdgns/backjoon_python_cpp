def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = 0
        for sk in skill_tree:
            if sk in skill:
                if skill[idx] == sk:
                    idx += 1
                else:
                    idx = -1
                    break
        if idx != -1:
            answer += 1
    return answer