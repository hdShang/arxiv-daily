---
layout: default
title: Mimicking Human Visual Development for Learning Robust Image Representations
---

# Mimicking Human Visual Development for Learning Robust Image Representations

**arXiv**: [2512.14360v1](https://arxiv.org/abs/2512.14360) | [PDF](https://arxiv.org/pdf/2512.14360.pdf)

**作者**: Ankita Raj, Kaashika Prajaapat, Tapan Kumar Gandhi, Chetan Arora

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Accepted to ICVGIP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/rajankita/Visual_Acuity_Curriculum)

---

## 💡 一句话要点

**提出渐进模糊课程学习，模仿人类视觉发育过程以提升卷积神经网络的泛化与鲁棒性。**

**关键词**: `渐进模糊课程学习` `人类视觉发育模仿` `卷积神经网络鲁棒性` `图像表示学习` `分布偏移适应` `对抗鲁棒性` `数据增强` `泛化能力提升`

## 📋 核心要点

1. 核心问题：现代卷积神经网络在适应输入分布变化方面表现不佳，缺乏人类视觉系统的鲁棒性，现有方法如静态模糊增强效果有限。
2. 方法要点：模仿人类视觉发育过程，提出渐进模糊课程学习，训练初期使用高度模糊图像，逐步减少模糊以引导网络学习全局结构。
3. 实验或效果：在CIFAR-10-C和ImageNet-100-C数据集上，平均腐蚀误差显著降低，泛化能力提升，且与现有增强技术兼容。

## 📝 摘要（中文）

人类视觉系统能出色适应输入分布变化，而现代卷积神经网络（CNNs）在此方面仍有不足。受人类视觉发育轨迹启发，本文提出一种渐进模糊课程学习方法来提升CNNs的泛化和鲁棒性。人类婴儿出生时视觉敏锐度较差，逐渐发展出感知细节的能力。模仿这一过程，我们在训练初期对CNNs使用高度模糊的图像，并随着训练进展逐步减少模糊程度。这种方法促使网络优先关注全局结构而非高频伪影，从而提升对分布偏移和噪声输入的鲁棒性。与先前认为早期模糊会造成刺激缺陷并不可逆损害模型性能的观点不同，我们发现早期模糊能增强泛化能力，对域内精度影响极小。实验表明，相比无模糊的标准训练，所提方法在CIFAR-10-C数据集上平均腐蚀误差（mCE）降低达8.30%，在ImageNet-100-C数据集上降低4.43%。与静态模糊增强（在整个训练中随机应用模糊图像）不同，我们的方法遵循结构化渐进过程，在不同数据集上均取得一致增益。此外，该方法可与其他增强技术（如CutMix和MixUp）互补，并提升对常见攻击方法的自然和对抗鲁棒性。代码已开源。

## 🔬 方法详解

论文提出一种渐进模糊课程学习框架，整体框架基于标准卷积神经网络训练流程，但引入动态模糊策略。关键技术创新点在于模仿人类视觉发育的渐进过程：训练初期使用高斯模糊等操作生成高度模糊图像作为输入，随着训练轮次增加，逐步降低模糊强度（如减小模糊核大小或标准差），直至最终使用清晰图像。这种方法的核心是结构化渐进，而非随机应用模糊。与现有方法的主要区别在于：不同于静态模糊增强（在整个训练中随机混合模糊和清晰图像），本方法遵循明确的课程顺序，从模糊到清晰，更贴合生物发育原理；同时，它挑战了早期模糊会损害性能的传统观点，通过实验证明早期模糊能促进泛化学习。

## 📊 实验亮点

实验显示，渐进模糊课程学习在CIFAR-10-C数据集上平均腐蚀误差（mCE）降低达8.30%，在ImageNet-100-C数据集上降低4.43%，显著优于无模糊标准训练。该方法还提升了对抗鲁棒性，与CutMix、MixUp等增强技术结合时效果更佳，验证了其泛化能力和实际应用价值。

## 🎯 应用场景

该研究可应用于计算机视觉领域中对鲁棒性要求高的场景，如自动驾驶中的图像识别（需处理天气变化、噪声干扰）、医疗影像分析（应对设备差异或图像质量波动）、安防监控（适应光照和视角变化）以及增强现实系统。通过提升模型对分布偏移和噪声的鲁棒性，有助于在实际部署中提高可靠性和安全性。

## 📄 摘要（原文）

> The human visual system is remarkably adept at adapting to changes in the input distribution; a capability modern convolutional neural networks (CNNs) still struggle to match. Drawing inspiration from the developmental trajectory of human vision, we propose a progressive blurring curriculum to improve the generalization and robustness of CNNs. Human infants are born with poor visual acuity, gradually refining their ability to perceive fine details. Mimicking this process, we begin training CNNs on highly blurred images during the initial epochs and progressively reduce the blur as training advances. This approach encourages the network to prioritize global structures over high-frequency artifacts, improving robustness against distribution shifts and noisy inputs. Challenging prior claims that blurring in the initial training epochs imposes a stimulus deficit and irreversibly harms model performance, we reveal that early-stage blurring enhances generalization with minimal impact on in-domain accuracy. Our experiments demonstrate that the proposed curriculum reduces mean corruption error (mCE) by up to 8.30% on CIFAR-10-C and 4.43% on ImageNet-100-C datasets, compared to standard training without blurring. Unlike static blur-based augmentation, which applies blurred images randomly throughout training, our method follows a structured progression, yielding consistent gains across various datasets. Furthermore, our approach complements other augmentation techniques, such as CutMix and MixUp, and enhances both natural and adversarial robustness against common attack methods. Code is available at https://github.com/rajankita/Visual_Acuity_Curriculum.

