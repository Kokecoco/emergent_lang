import gymnasium as gym
import time

# CartPole環境を作成します。render_mode="human" にすると画面が表示されます。
# ウィンドウが表示されない場合、gymnasium-box2dのインストールが必要かもしれません。
# その場合はターミナルで pip install gymnasium[box2d] を実行してください。
try:
    env = gym.make("CartPole-v1", render_mode="human")
except Exception as e:
    print(f"エラー: {e}")
    print("ウィンドウ表示で問題が発生した場合、ターミナルで以下のコマンドを実行してみてください。")
    print("pip install gymnasium[box2d]")
    exit()

# 環境を初期化（リセット）します。
observation, info = env.reset(seed=42) # seedを固定すると毎回同じ初期状態になります

# 5エピソード分、シミュレーションを実行します
for episode in range(10):
    print(f"エピソード {episode + 1} を開始します。")
    # 1エピソードは最大500ステップ
    for step in range(500):
        # 環境を描画します
        env.render()

        # 行動をランダムに選択します (0: 左に押す, 1: 右に押す)
        action = env.action_space.sample()

        # 選択した行動を実行し、次の状態、報酬、終了フラグなどを取得します
        observation, reward, terminated, truncated, info = env.step(action)

        # もしエピソードが終了（棒が倒れたなど）したら
        if terminated or truncated:
            print(f"  ステップ {step + 1} でエピソード終了。")
            # 環境をリセットして、次のエピソードを開始します
            observation, info = env.reset(seed=42 + episode + 1)
            break # このforループを抜けて、次のエピソードへ

        # 人間が見やすいように少しだけ待機
        time.sleep(0.01)

# 環境をクローズします
env.close()
print("\nシミュレーション完了。")