import pygame
import pygame.freetype
from pettingzoo.mpe import simple_speaker_listener_v4
import time

# 環境の初期化
env = simple_speaker_listener_v4.parallel_env(render_mode="human")
observations, infos = env.reset()

# 動作確認のため、少しループさせてみる
try:
    for _ in range(100):
        # ランダムな行動を選択
        actions = {agent: env.action_space(agent).sample() for agent in env.agents}
        
        # 環境を1ステップ進める
        observations, rewards, terminations, truncations, infos = env.step(actions)
        
        # 画面描画のための待機（早すぎると見えないため）
        time.sleep(0.05)
        
        # すべてのエージェントが終了したらリセット
        if all(terminations.values()) or all(truncations.values()):
            observations, infos = env.reset()

finally:
    env.close()
    print("実行が完了しました")