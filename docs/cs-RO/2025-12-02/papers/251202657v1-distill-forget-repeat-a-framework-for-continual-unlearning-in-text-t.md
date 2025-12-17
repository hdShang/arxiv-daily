---
layout: default
title: Distill, Forget, Repeat: A Framework for Continual Unlearning in Text-to-Image Diffusion Models
---

# Distill, Forget, Repeat: A Framework for Continual Unlearning in Text-to-Image Diffusion Models

**arXiv**: [2512.02657v1](https://arxiv.org/abs/2512.02657) | [PDF](https://arxiv.org/pdf/2512.02657.pdf)

**作者**: Naveen George, Naoki Murata, Yuhta Takida, Konda Reddy Mopuri, Yuki Mitsufuji

---

## 💡 一句话要点

**提出基于生成蒸馏的持续遗忘框架，以解决文本到图像扩散模型中的序列删除请求问题。**

**关键词**: `持续遗忘` `文本到图像扩散模型` `机器遗忘` `生成蒸馏` `多目标优化` `模型稳定性`

## 📋 核心要点

1. 核心问题：现有机器遗忘方法无法处理序列删除请求，导致模型稳定性和生成质量下降。
2. 方法要点：将每个遗忘步骤重构为多目标师生蒸馏过程，结合持续学习原则保持模型完整性。
3. 实验或效果：在10步序列基准测试中，有效遗忘目标概念，同时保持保留概念性能和整体图像质量。

## 📄 摘要（原文）

> The recent rapid growth of visual generative models trained on vast web-scale datasets has created significant tension with data privacy regulations and copyright laws, such as GDPR's ``Right to be Forgotten.'' This necessitates machine unlearning (MU) to remove specific concepts without the prohibitive cost of retraining. However, existing MU techniques are fundamentally ill-equipped for real-world scenarios where deletion requests arrive sequentially, a setting known as continual unlearning (CUL). Naively applying one-shot methods in a continual setting triggers a stability crisis, leading to a cascade of degradation characterized by retention collapse, compounding collateral damage to related concepts, and a sharp decline in generative quality. To address this critical challenge, we introduce a novel generative distillation based continual unlearning framework that ensures targeted and stable unlearning under sequences of deletion requests. By reframing each unlearning step as a multi-objective, teacher-student distillation process, the framework leverages principles from continual learning to maintain model integrity. Experiments on a 10-step sequential benchmark demonstrate that our method unlearns forget concepts with better fidelity and achieves this without significant interference to the performance on retain concepts or the overall image quality, substantially outperforming baselines. This framework provides a viable pathway for the responsible deployment and maintenance of large-scale generative models, enabling industries to comply with ongoing data removal requests in a practical and effective manner.

