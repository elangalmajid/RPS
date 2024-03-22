def player(prev_play, opp_history=[], play_order={}):
  if not prev_play:
      prev_play = 'R'

  opp_history.append(prev_play)
  predict = 'P'

  if len(opp_history) > 4:
      last_five = "".join(opp_history[-5:])
      play_order[last_five] = play_order.get(last_five, 0) + 1

      potential = [
          "".join([*opp_history[-4:], v]) 
          for v in ['R', 'P', 'S']
      ]

      sub_order = {
          k: play_order[k]
          for k in potential if k in play_order
      }

      if sub_order:
          predict = max(sub_order, key=sub_order.get)[-1:]

  response = {'P': 'S', 'R': 'P', 'S': 'R'}

  return response[predict]