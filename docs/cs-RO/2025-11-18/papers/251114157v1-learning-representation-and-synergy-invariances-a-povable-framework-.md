---
layout: default
title: Learning Representation and Synergy Invariances: A Povable Framework for Generalized Multimodal Face Anti-Spoofing
---

# Learning Representation and Synergy Invariances: A Povable Framework for Generalized Multimodal Face Anti-Spoofing

**arXiv**: [2511.14157v1](https://arxiv.org/abs/2511.14157) | [PDF](https://arxiv.org/pdf/2511.14157.pdf)

**作者**: Xun Lin, Shuai Wang, Yi Yu, Zitong Yu, Jiale Zhou, Yizhong Liu, Xiaochun Cao, Alex Kot, Yefeng Zheng

---

## 💡 一句话要点

**提出RiSe框架以解决多模态人脸防伪的跨域泛化问题**

**关键词**: `多模态人脸防伪` `跨域泛化` `表示不变性` `协同不变性` `自监督学习` `理论分析`

## 📋 核心要点

1. 多模态人脸防伪在未知域性能下降，源于表示和协同不变性风险
2. RiSe框架结合AsyIRM和MMSD，学习不变表示和协同特征
3. 理论分析和实验验证RiSe在跨域性能上达到最优

## 📄 摘要（原文）

> Multimodal Face Anti-Spoofing (FAS) methods, which integrate multiple visual modalities, often suffer even more severe performance degradation than unimodal FAS when deployed in unseen domains. This is mainly due to two overlooked risks that affect cross-domain multimodal generalization. The first is the modal representation invariant risk, i.e., whether representations remain generalizable under domain shift. We theoretically show that the inherent class asymmetry in FAS (diverse spoofs vs. compact reals) enlarges the upper bound of generalization error, and this effect is further amplified in multimodal settings. The second is the modal synergy invariant risk, where models overfit to domain-specific inter-modal correlations. Such spurious synergy cannot generalize to unseen attacks in target domains, leading to performance drops. To solve these issues, we propose a provable framework, namely Multimodal Representation and Synergy Invariance Learning (RiSe). For representation risk, RiSe introduces Asymmetric Invariant Risk Minimization (AsyIRM), which learns an invariant spherical decision boundary in radial space to fit asymmetric distributions, while preserving domain cues in angular space. For synergy risk, RiSe employs Multimodal Synergy Disentanglement (MMSD), a self-supervised task enhancing intrinsic, generalizable modal features via cross-sample mixing and disentanglement. Theoretical analysis and experiments verify RiSe, which achieves state-of-the-art cross-domain performance.

