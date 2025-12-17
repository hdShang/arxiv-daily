---
layout: default
title: EvoVLA: Self-Evolving Vision-Language-Action Model
---

# EvoVLA: Self-Evolving Vision-Language-Action Model

**arXiv**: [2511.16166v1](https://arxiv.org/abs/2511.16166) | [PDF](https://arxiv.org/pdf/2511.16166.pdf)

**作者**: Zeting Liu, Zida Yang, Zeyu Zhang, Hao Tang

---

## 💡 一句话要点

**提出EvoVLA自进化视觉-语言-动作模型，解决长程机器人操作中的阶段幻觉问题。**

**关键词**: `视觉-语言-动作模型` `长程机器人操作` `阶段幻觉` `自监督学习` `模拟到真实迁移`

## 📋 核心要点

1. 核心问题：VLA模型在长程操作中易出现阶段幻觉，利用粗评估信号走捷径。
2. 方法要点：结合阶段对齐奖励、姿态对象探索和长程记忆，提升任务完成真实性。
3. 实验或效果：在Discoverse-L基准上，任务成功率提升10.2个百分点，达69.2%。

## 📄 摘要（原文）

> Long-horizon robotic manipulation remains challenging for Vision-Language-Action (VLA) models despite recent progress in zero-shot generalization and simulation-to-real-world transfer. Current VLA models suffer from stage hallucination, where agents exploit coarse evaluation signals to shortcut multi-step tasks, reporting high progress without truly completing them. We present EvoVLA, a self-supervised VLA framework that addresses this issue through three complementary components: Stage-Aligned Reward (SAR), which uses triplet contrastive learning with Gemini-generated hard negatives to prevent visual shortcuts; Pose-Based Object Exploration (POE), which grounds curiosity in relative object-gripper pose instead of raw pixels; and Long-Horizon Memory, which uses selective context retention and gated fusion to stabilize intrinsic shaping during extended rollouts. Extensive evaluations on Discoverse-L, a long-horizon manipulation benchmark with three multi-stage tasks, show that EvoVLA improves average task success by 10.2 percentage points over the strongest baseline (OpenVLA-OFT), reaching 69.2 percent. EvoVLA also achieves one-and-a-half times better sample efficiency and reduces stage hallucination from 38.5 percent to 14.8 percent. Real-world deployment on physical robots reaches an average success rate of 54.6 percent across four manipulation tasks, outperforming OpenVLA-OFT by 11 points, demonstrating effective sim-to-real transfer and strong generalization. Code: https://github.com/AIGeeksGroup/EvoVLA. Website: https://aigeeksgroup.github.io/EvoVLA.

