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

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `渐进模糊课程学习` `人类视觉发育模拟` `卷积神经网络鲁棒性` `分布偏移适应` `图像增强技术` `泛化能力提升` `对抗鲁棒性` `课程学习策略`

## 📋 核心要点

1. 核心问题：现代卷积神经网络在适应输入分布变化方面不如人类视觉系统鲁棒，易受分布偏移和噪声影响。
2. 方法要点：模仿人类视觉发育，设计渐进模糊课程，从高度模糊图像开始训练并逐步减少模糊，引导网络学习全局结构。
3. 实验或效果：在CIFAR-10-C和ImageNet-100-C上显著降低平均腐蚀误差，提升泛化能力且不影响域内精度。

## 📝 摘要（中文）

人类视觉系统能出色适应输入分布变化，而现代卷积神经网络（CNNs）在这方面仍有不足。受人类视觉发育轨迹启发，我们提出一种渐进模糊课程学习方法来提升CNNs的泛化能力和鲁棒性。人类婴儿出生时视觉敏锐度较差，逐渐发展出感知细节的能力。模仿这一过程，我们在训练初期使用高度模糊的图像训练CNNs，随着训练推进逐步减少模糊程度。这种方法促使网络优先关注全局结构而非高频伪影，从而提升对分布偏移和噪声输入的鲁棒性。与先前认为早期模糊会造成刺激缺陷并不可逆损害模型性能的观点不同，我们发现早期模糊能增强泛化能力，对域内精度影响极小。实验表明，相比无模糊的标准训练，所提方法在CIFAR-10-C数据集上平均腐蚀误差（mCE）降低达8.30%，在ImageNet-100-C数据集上降低4.43%。与静态模糊增强（在整个训练中随机应用模糊图像）不同，我们的方法遵循结构化渐进过程，在不同数据集上均取得一致提升。此外，该方法可与其他增强技术（如CutMix和MixUp）互补，并提升对常见攻击方法的自然和对抗鲁棒性。代码已开源。

## 🔬 方法详解

整体框架基于标准卷积神经网络训练，但引入渐进模糊课程作为预处理步骤。关键技术创新点在于模拟人类视觉发育过程：训练初期对输入图像应用强高斯模糊，随着训练轮次增加，逐步降低模糊强度直至为零，形成从模糊到清晰的动态课程。与现有方法的主要区别在于：不同于静态模糊增强（在整个训练中随机应用模糊），该方法采用结构化渐进策略；且与先前认为早期模糊有害的观点相反，证明了早期模糊能促进泛化学习。

## 📊 实验亮点

在CIFAR-10-C数据集上平均腐蚀误差降低8.30%，在ImageNet-100-C上降低4.43%；与CutMix、MixUp等增强技术兼容，进一步提升自然和对抗鲁棒性；实验验证了早期模糊对泛化的积极影响，反驳了相关负面观点。

## 🎯 应用场景

该研究可应用于需要高鲁棒性的计算机视觉任务，如自动驾驶中的环境感知、医疗图像分析中的噪声鲁棒分类、安防监控中的抗干扰识别，以及任何面临分布偏移或对抗攻击的场景，提升模型在实际复杂环境中的可靠性。

## 📄 摘要（原文）

> The human visual system is remarkably adept at adapting to changes in the input distribution; a capability modern convolutional neural networks (CNNs) still struggle to match. Drawing inspiration from the developmental trajectory of human vision, we propose a progressive blurring curriculum to improve the generalization and robustness of CNNs. Human infants are born with poor visual acuity, gradually refining their ability to perceive fine details. Mimicking this process, we begin training CNNs on highly blurred images during the initial epochs and progressively reduce the blur as training advances. This approach encourages the network to prioritize global structures over high-frequency artifacts, improving robustness against distribution shifts and noisy inputs. Challenging prior claims that blurring in the initial training epochs imposes a stimulus deficit and irreversibly harms model performance, we reveal that early-stage blurring enhances generalization with minimal impact on in-domain accuracy. Our experiments demonstrate that the proposed curriculum reduces mean corruption error (mCE) by up to 8.30% on CIFAR-10-C and 4.43% on ImageNet-100-C datasets, compared to standard training without blurring. Unlike static blur-based augmentation, which applies blurred images randomly throughout training, our method follows a structured progression, yielding consistent gains across various datasets. Furthermore, our approach complements other augmentation techniques, such as CutMix and MixUp, and enhances both natural and adversarial robustness against common attack methods. Code is available at https://github.com/rajankita/Visual_Acuity_Curriculum.

