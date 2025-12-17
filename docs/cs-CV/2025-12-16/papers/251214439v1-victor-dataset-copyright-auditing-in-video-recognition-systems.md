---
layout: default
title: VICTOR: Dataset Copyright Auditing in Video Recognition Systems
---

# VICTOR: Dataset Copyright Auditing in Video Recognition Systems

**arXiv**: [2512.14439v1](https://arxiv.org/abs/2512.14439) | [PDF](https://arxiv.org/pdf/2512.14439.pdf)

**作者**: Quan Yuan, Zhikun Zhang, Linkang Du, Min Chen, Mingyang Sun, Yunjun Gao, Shibo He, Jiming Chen

**分类**: cs.CR, cs.CV

**发布日期**: 2025-12-16

**备注**: To appear in the NDSS Symposium 2026, February 2026, San Diego, CA, USA

---

## 💡 一句话要点

**提出VICTOR方法以解决视频识别系统中数据集版权审计的挑战**

**关键词**: `视频识别系统` `数据集版权审计` `样本修改策略` `模型行为差异` `时间维度挑战` `隐蔽性审计` `鲁棒性验证` `视频数据保护`

## 📋 核心要点

1. 现有方法主要针对图像领域，视频数据的时间维度带来有效性和隐蔽性挑战，导致视频数据集版权审计未被充分探索。
2. 提出VICTOR方法，通过隐蔽修改少量样本（如1%）来放大模型输出差异，利用行为差异作为审计依据。
3. 在多个模型和数据集上实验显示VICTOR具有优越性能，且对训练视频或模型的扰动机制保持鲁棒性。

## 📝 摘要（中文）

视频识别系统在内容推荐和安全监控等日常应用中日益普及。为促进视频识别技术的发展，许多机构发布了高质量的开源公共数据集用于训练先进模型。然而，这些数据集也容易遭到滥用和侵权。数据集版权审计是识别此类未经授权使用的有效解决方案。但现有的数据集版权解决方案主要集中于图像领域；视频数据的复杂性使得视频领域的数据集版权审计尚未得到充分探索。具体而言，视频数据引入了额外的时间维度，这对现有方法的有效性和隐蔽性构成了重大挑战。本文提出了VICTOR，这是首个针对视频识别系统的数据集版权审计方法。我们开发了一种通用且隐蔽的样本修改策略，增强了目标模型的输出差异。通过仅修改一小部分样本（例如1%），VICTOR放大了已发布修改样本对目标模型预测行为的影响。然后，模型对已发布修改样本和未发布原始样本的行为差异可作为数据集审计的关键依据。在多个模型和数据集上的广泛实验突显了VICTOR的优越性。最后，我们展示了VICTOR在面对训练视频或目标模型的多种扰动机制时具有鲁棒性。

## 🔬 方法详解

VICTOR的整体框架基于一种通用且隐蔽的样本修改策略，旨在增强目标模型在已发布修改样本和未发布原始样本之间的输出差异。关键技术创新点在于设计了一种高效的修改机制，仅需修改少量样本（如1%），即可显著放大模型预测行为的变化，从而在不影响模型正常使用的前提下实现审计。与现有方法的主要区别在于，VICTOR专门针对视频数据的时空特性进行优化，克服了时间维度带来的挑战，而现有方法多局限于静态图像领域，缺乏对视频复杂性的处理能力。

## 📊 实验亮点

实验表明，VICTOR在多个视频识别模型和数据集上均表现出优越的审计性能，仅修改1%样本即可有效放大模型输出差异，且在面对训练视频或模型的扰动时保持鲁棒，验证了其在实际场景中的实用性和可靠性。

## 🎯 应用场景

该研究可应用于视频识别系统的数据集版权保护，例如在内容推荐、安全监控等领域，帮助机构检测未经授权的数据集使用，维护知识产权，促进视频数据资源的合法共享和利用。

## 📄 摘要（原文）

> Video recognition systems are increasingly being deployed in daily life, such as content recommendation and security monitoring. To enhance video recognition development, many institutions have released high-quality public datasets with open-source licenses for training advanced models. At the same time, these datasets are also susceptible to misuse and infringement. Dataset copyright auditing is an effective solution to identify such unauthorized use. However, existing dataset copyright solutions primarily focus on the image domain; the complex nature of video data leaves dataset copyright auditing in the video domain unexplored. Specifically, video data introduces an additional temporal dimension, which poses significant challenges to the effectiveness and stealthiness of existing methods.
>   In this paper, we propose VICTOR, the first dataset copyright auditing approach for video recognition systems. We develop a general and stealthy sample modification strategy that enhances the output discrepancy of the target model. By modifying only a small proportion of samples (e.g., 1%), VICTOR amplifies the impact of published modified samples on the prediction behavior of the target models. Then, the difference in the model's behavior for published modified and unpublished original samples can serve as a key basis for dataset auditing. Extensive experiments on multiple models and datasets highlight the superiority of VICTOR. Finally, we show that VICTOR is robust in the presence of several perturbation mechanisms to the training videos or the target models.

