---
layout: default
title: Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation
---

# Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation

**arXiv**: [2512.08186v1](https://arxiv.org/abs/2512.08186) | [PDF](https://arxiv.org/pdf/2512.08186.pdf)

**作者**: Meng Wei, Chenyang Wan, Jiaqi Peng, Xiqian Yu, Yuqiang Yang, Delin Feng, Wenzhe Cai, Chenming Zhu, Tai Wang, Jiangmiao Pang, Xihui Liu

---

## 💡 一句话要点

**提出DualVLN双系统基础模型，通过高低层协同解决视觉语言导航中的碎片化动作和动态环境适应问题。**

**关键词**: `视觉语言导航` `双系统模型` `扩散Transformer` `实时控制` `动态环境适应` `基础模型`

## 📋 核心要点

1. 现有端到端方法在视觉语言导航中产生碎片化动作，延迟高且难以应对动态障碍。
2. DualVLN结合基于VLM的全局规划器和轻量级扩散Transformer策略，实现高低层推理与执行协同。
3. 在VLN基准测试和真实世界实验中，模型表现优于先前方法，支持实时适应和长程规划。

## 📄 摘要（原文）

> While recent large vision-language models (VLMs) have improved generalization in vision-language navigation (VLN), existing methods typically rely on end-to-end pipelines that map vision-language inputs directly to short-horizon discrete actions. Such designs often produce fragmented motions, incur high latency, and struggle with real-world challenges like dynamic obstacle avoidance. We propose DualVLN, the first dual-system VLN foundation model that synergistically integrates high-level reasoning with low-level action execution. System 2, a VLM-based global planner, "grounds slowly" by predicting mid-term waypoint goals via image-grounded reasoning. System 1, a lightweight, multi-modal conditioning Diffusion Transformer policy, "moves fast" by leveraging both explicit pixel goals and latent features from System 2 to generate smooth and accurate trajectories. The dual-system design enables robust real-time control and adaptive local decision-making in complex, dynamic environments. By decoupling training, the VLM retains its generalization, while System 1 achieves interpretable and effective local navigation. DualVLN outperforms prior methods across all VLN benchmarks and real-world experiments demonstrate robust long-horizon planning and real-time adaptability in dynamic environments.

