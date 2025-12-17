---
layout: default
title: A Single Set of Adversarial Clothes Breaks Multiple Defense Methods in the Physical World
---

# A Single Set of Adversarial Clothes Breaks Multiple Defense Methods in the Physical World

**arXiv**: [2510.17322v1](https://arxiv.org/abs/2510.17322) | [PDF](https://arxiv.org/pdf/2510.17322.pdf)

**作者**: Wei Zhang, Zhanhao Hu, Xiao Li, Xiaopei Zhu, Xiaolin Hu

---

## 💡 一句话要点

**提出对抗性衣物攻击，揭示多种防御方法在物理世界中的共同脆弱性。**

**关键词**: `对抗攻击` `物理世界防御` `对象检测` `对抗衣物` `攻击成功率` `深度学习安全`

## 📋 核心要点

1. 核心问题：现有防御方法对基于补丁的物理世界对抗攻击存在漏洞，尤其在大尺寸攻击下。
2. 方法要点：通过扩大补丁尺寸并设计自然外观的对抗性衣物，评估多种防御方法的鲁棒性。
3. 实验或效果：单一对抗衣物在物理世界中攻击成功率高达96.06%，对九种防御模型均超过64.84%。

## 📄 摘要（原文）

> In recent years, adversarial attacks against deep learning-based object
> detectors in the physical world have attracted much attention. To defend
> against these attacks, researchers have proposed various defense methods
> against adversarial patches, a typical form of physically-realizable attack.
> However, our experiments showed that simply enlarging the patch size could make
> these defense methods fail. Motivated by this, we evaluated various defense
> methods against adversarial clothes which have large coverage over the human
> body. Adversarial clothes provide a good test case for adversarial defense
> against patch-based attacks because they not only have large sizes but also
> look more natural than a large patch on humans. Experiments show that all the
> defense methods had poor performance against adversarial clothes in both the
> digital world and the physical world. In addition, we crafted a single set of
> clothes that broke multiple defense methods on Faster R-CNN. The set achieved
> an Attack Success Rate (ASR) of 96.06% against the undefended detector and over
> 64.84% ASRs against nine defended models in the physical world, unveiling the
> common vulnerability of existing adversarial defense methods against
> adversarial clothes. Code is available at:
> https://github.com/weiz0823/adv-clothes-break-multiple-defenses.

