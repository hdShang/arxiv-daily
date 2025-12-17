---
layout: default
title: Diversifying Counterattacks: Orthogonal Exploration for Robust CLIP Inference
---

# Diversifying Counterattacks: Orthogonal Exploration for Robust CLIP Inference

**arXiv**: [2511.09064v1](https://arxiv.org/abs/2511.09064) | [PDF](https://arxiv.org/pdf/2511.09064.pdf)

**作者**: Chengze Jiang, Minjing Dong, Xinli Shi, Jie Gui

---

## 💡 一句话要点

**提出方向正交反攻击以增强CLIP推理的对抗鲁棒性**

**关键词**: `对抗鲁棒性` `视觉语言预训练` `反攻击方法` `正交梯度` `测试时防御` `CLIP模型`

## 📋 核心要点

1. 核心问题：对抗样本使视觉语言预训练模型易受攻击，现有反攻击方法缺乏多样性。
2. 方法要点：引入正交梯度方向和动量更新，扩展反攻击空间探索。
3. 实验或效果：在16个数据集上验证，提升对抗鲁棒性并保持清洁准确率。

## 📄 摘要（原文）

> Vision-language pre-training models (VLPs) demonstrate strong multimodal understanding and zero-shot generalization, yet remain vulnerable to adversarial examples, raising concerns about their reliability. Recent work, Test-Time Counterattack (TTC), improves robustness by generating perturbations that maximize the embedding deviation of adversarial inputs using PGD, pushing them away from their adversarial representations. However, due to the fundamental difference in optimization objectives between adversarial attacks and counterattacks, generating counterattacks solely based on gradients with respect to the adversarial input confines the search to a narrow space. As a result, the counterattacks could overfit limited adversarial patterns and lack the diversity to fully neutralize a broad range of perturbations. In this work, we argue that enhancing the diversity and coverage of counterattacks is crucial to improving adversarial robustness in test-time defense. Accordingly, we propose Directional Orthogonal Counterattack (DOC), which augments counterattack optimization by incorporating orthogonal gradient directions and momentum-based updates. This design expands the exploration of the counterattack space and increases the diversity of perturbations, which facilitates the discovery of more generalizable counterattacks and ultimately improves the ability to neutralize adversarial perturbations. Meanwhile, we present a directional sensitivity score based on averaged cosine similarity to boost DOC by improving example discrimination and adaptively modulating the counterattack strength. Extensive experiments on 16 datasets demonstrate that DOC improves adversarial robustness under various attacks while maintaining competitive clean accuracy. Code is available at https://github.com/bookman233/DOC.

