---
layout: default
title: Robust Defense Strategies for Multimodal Contrastive Learning: Efficient Fine-tuning Against Backdoor Attacks
---

# Robust Defense Strategies for Multimodal Contrastive Learning: Efficient Fine-tuning Against Backdoor Attacks

**arXiv**: [2511.13545v1](https://arxiv.org/abs/2511.13545) | [PDF](https://arxiv.org/pdf/2511.13545.pdf)

**作者**: Md. Iqbal Hossain, Afia Sajeeda, Neeresh Kumar Perla, Ming Shao

---

## 💡 一句话要点

**提出高效微调策略以防御多模态对比学习中的后门攻击**

**关键词**: `多模态对比学习` `后门攻击防御` `CLIP模型` `图像分割oracle` `高效微调` `视觉识别`

## 📋 核心要点

1. 多模态模型如CLIP易受后门攻击，现有防御方法效率低且不精确
2. 引入图像分割oracle监督，识别触发器和受害样本，构建紧凑微调数据集
3. 在视觉识别基准上验证策略有效，能消除后门影响

## 📄 摘要（原文）

> The advent of multimodal deep learning models, such as CLIP, has unlocked new frontiers in a wide range of applications, from image-text understanding to classification tasks. However, these models are not safe for adversarial attacks, particularly backdoor attacks, which can subtly manipulate model behavior. Moreover, existing defense methods typically involve training from scratch or fine-tuning using a large dataset without pinpointing the specific labels that are affected. In this study, we introduce an innovative strategy to enhance the robustness of multimodal contrastive learning models against such attacks. In particular, given a poisoned CLIP model, our approach can identify the backdoor trigger and pinpoint the victim samples and labels in an efficient manner. To that end, an image segmentation ``oracle'' is introduced as the supervisor for the output of the poisoned CLIP. We develop two algorithms to rectify the poisoned model: (1) differentiating between CLIP and Oracle's knowledge to identify potential triggers; (2) pinpointing affected labels and victim samples, and curating a compact fine-tuning dataset. With this knowledge, we are allowed to rectify the poisoned CLIP model to negate backdoor effects. Extensive experiments on visual recognition benchmarks demonstrate our strategy is effective in CLIP-based backdoor defense.

