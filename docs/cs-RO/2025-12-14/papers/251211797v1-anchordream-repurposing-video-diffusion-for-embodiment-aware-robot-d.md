---
layout: default
title: AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis
---

# AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis

**arXiv**: [2512.11797v1](https://arxiv.org/abs/2512.11797) | [PDF](https://arxiv.org/pdf/2512.11797.pdf)

**作者**: Junjie Ye, Rong Xue, Basile Van Hoorick, Pavel Tokmakov, Muhammad Zubair Irshad, Yue Wang, Vitor Guizilini

---

## 💡 一句话要点

**提出AnchorDream，通过视频扩散模型合成机器人数据以解决模仿学习数据瓶颈问题。**

**关键词**: `机器人数据合成` `视频扩散模型` `模仿学习` `仿真到现实迁移` `生成模型`

## 📋 核心要点

1. 核心问题：机器人模仿学习面临大规模多样化数据获取成本高、仿真器多样性有限且存在仿真到现实差距。
2. 方法要点：利用预训练视频扩散模型，以机器人运动渲染为条件，合成与机器人运动学一致的对象和环境数据。
3. 实验或效果：生成数据提升下游策略学习性能，在仿真基准中相对增益36.4%，真实世界性能近翻倍。

## 📄 摘要（原文）

> The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

