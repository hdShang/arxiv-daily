---
layout: default
title: Fragile by Design: On the Limits of Adversarial Defenses in Personalized Generation
---

# Fragile by Design: On the Limits of Adversarial Defenses in Personalized Generation

**arXiv**: [2511.10382v1](https://arxiv.org/abs/2511.10382) | [PDF](https://arxiv.org/pdf/2511.10382.pdf)

**作者**: Zhen Chen, Yi Zhang, Xiangyu Yin, Chengxuan Qin, Xingyu Zhao, Xiaowei Huang, Wenjie Ruan

---

## 💡 一句话要点

**揭示个性化生成中对抗防御的脆弱性，提出评估框架以测试净化威胁。**

**关键词**: `个性化生成` `对抗防御` `隐私保护` `图像净化` `身份泄露` `评估框架`

## 📋 核心要点

1. 核心问题：个性化AI应用如DreamBooth存在面部身份泄露隐私风险，现有防御机制易被检测和移除。
2. 方法要点：提出AntiDB_Purify框架，系统评估防御方法在传统图像过滤和对抗净化下的有效性。
3. 实验或效果：结果显示当前防御方法在净化威胁下均失效，强调需更隐蔽和鲁棒的保护措施。

## 📄 摘要（原文）

> Personalized AI applications such as DreamBooth enable the generation of customized content from user images, but also raise significant privacy concerns, particularly the risk of facial identity leakage. Recent defense mechanisms like Anti-DreamBooth attempt to mitigate this risk by injecting adversarial perturbations into user photos to prevent successful personalization. However, we identify two critical yet overlooked limitations of these methods. First, the adversarial examples often exhibit perceptible artifacts such as conspicuous patterns or stripes, making them easily detectable as manipulated content. Second, the perturbations are highly fragile, as even a simple, non-learned filter can effectively remove them, thereby restoring the model's ability to memorize and reproduce user identity. To investigate this vulnerability, we propose a novel evaluation framework, AntiDB_Purify, to systematically evaluate existing defenses under realistic purification threats, including both traditional image filters and adversarial purification. Results reveal that none of the current methods maintains their protective effectiveness under such threats. These findings highlight that current defenses offer a false sense of security and underscore the urgent need for more imperceptible and robust protections to safeguard user identity in personalized generation.

