---
layout: default
title: ANCHOR: Integrating Adversarial Training with Hard-mined Supervised Contrastive Learning for Robust Representation Learning
---

# ANCHOR: Integrating Adversarial Training with Hard-mined Supervised Contrastive Learning for Robust Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27599" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27599v1</a>
  <a href="https://arxiv.org/pdf/2510.27599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27599v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27599v1', 'ANCHOR: Integrating Adversarial Training with Hard-mined Supervised Contrastive Learning for Robust Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samarup Bhattacharya, Anubhab Bhattacharya, Abir Chakraborty

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: 11 pages, 1 figure

---

## 💡 一句话要点

**提出ANCHOR框架，结合对抗训练与难例监督对比学习，提升表征学习的鲁棒性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `对抗训练` `监督对比学习` `难例挖掘` `鲁棒表征学习` `深度学习` `对抗攻击` `图像分类`

## 📋 核心要点

1. 神经网络易受对抗攻击，微小扰动即可导致错误预测，现有方法难以兼顾准确率和鲁棒性。
2. ANCHOR框架结合对抗训练与监督对比学习，通过难例挖掘，使同类图像及其扰动在嵌入空间聚集。
3. 实验表明，ANCHOR在CIFAR-10上显著提升了对抗环境下的准确率，优于标准对抗训练方法。

## 📝 摘要（中文）

神经网络通过梯度下降学习数据中的判别模式，但也因此存在对抗攻击的漏洞。微小的、难以察觉的扰动就能导致模型做出错误判断。本文提出了对抗训练的对比硬挖掘优化鲁棒性框架（ANCHOR）。该框架利用监督对比学习和显式的难正例挖掘，使模型学习到的图像表征能够将图像本身、其增强版本以及扰动版本，与同类别的其他图像在嵌入空间中聚集在一起，同时与其他类别的图像分离。这种对齐有助于模型关注稳定、有意义的模式，而不是脆弱的梯度线索。在CIFAR-10数据集上，我们的方法在PGD-20（epsilon = 0.031）攻击下，实现了令人印象深刻的干净准确率和鲁棒准确率，优于标准对抗训练方法。结果表明，将对抗指导与硬挖掘对比监督相结合，有助于模型学习更结构化和鲁棒的表征，缩小准确率和鲁棒性之间的差距。

## 🔬 方法详解

**问题定义**：论文旨在解决深度学习模型在对抗攻击下的脆弱性问题。现有对抗训练方法虽然能提高模型的鲁棒性，但往往会牺牲在干净数据上的准确率。此外，现有方法在学习鲁棒表征时，可能无法充分利用类别信息，导致学习到的表征区分性不足。

**核心思路**：论文的核心思路是将对抗训练与监督对比学习相结合，并引入难例挖掘机制。通过对抗训练，模型可以学习抵抗微小扰动的能力。监督对比学习则利用类别信息，促使同类样本在嵌入空间中聚集，不同类样本分离。难例挖掘则关注那些容易被误分类的样本，从而进一步提升模型的区分能力和鲁棒性。

**技术框架**：ANCHOR框架主要包含三个组成部分：图像增强模块、对抗样本生成模块和对比学习模块。首先，对输入图像进行增强，生成多个增强样本。然后，利用对抗攻击算法（如PGD）生成对抗样本。最后，将原始图像、增强样本和对抗样本输入到编码器中，得到它们的嵌入向量。对比学习模块利用这些嵌入向量，计算对比损失，并更新模型参数。

**关键创新**：论文的关键创新在于将对抗训练、监督对比学习和难例挖掘有机结合。传统的对抗训练主要关注单个样本的分类正确性，而ANCHOR则关注样本之间的关系，通过对比学习，使模型学习到更具区分性的表征。难例挖掘则进一步提升了模型的鲁棒性。

**关键设计**：ANCHOR框架的关键设计包括：1) 使用监督对比损失函数，鼓励同类样本的嵌入向量聚集，不同类样本分离。2) 采用难例挖掘策略，选择那些距离较近的同类样本作为难正例，并将其纳入对比损失的计算中。3) 使用对抗训练生成对抗样本，并将其作为对比学习的输入，从而提升模型的鲁棒性。具体的损失函数包括对比损失和交叉熵损失，通过加权求和进行优化。

## 📊 实验亮点

在CIFAR-10数据集上，ANCHOR在PGD-20攻击下，实现了优于标准对抗训练方法的鲁棒准确率。具体而言，ANCHOR在保持较高干净数据准确率的同时，显著提升了对抗环境下的准确率，缩小了准确率和鲁棒性之间的差距。实验结果表明，结合对抗指导与硬挖掘对比监督能够有效提升模型的鲁棒性。

## 🎯 应用场景

该研究成果可应用于对安全性要求较高的领域，如自动驾驶、医疗诊断和金融风控等。在这些领域，模型需要能够抵抗恶意攻击，保证决策的可靠性。通过提升模型的鲁棒性，可以有效降低模型被攻击的风险，提高系统的安全性。

## 📄 摘要（原文）

> Neural networks have changed the way machines interpret the world. At their core, they learn by following gradients, adjusting their parameters step by step until they identify the most discriminant patterns in the data. This process gives them their strength, yet it also opens the door to a hidden flaw. The very gradients that help a model learn can also be used to produce small, imperceptible tweaks that cause the model to completely alter its decision. Such tweaks are called adversarial attacks. These attacks exploit this vulnerability by adding tiny, imperceptible changes to images that, while leaving them identical to the human eye, cause the model to make wrong predictions. In this work, we propose Adversarially-trained Contrastive Hard-mining for Optimized Robustness (ANCHOR), a framework that leverages the power of supervised contrastive learning with explicit hard positive mining to enable the model to learn representations for images such that the embeddings for the images, their augmentations, and their perturbed versions cluster together in the embedding space along with those for other images of the same class while being separated from images of other classes. This alignment helps the model focus on stable, meaningful patterns rather than fragile gradient cues. On CIFAR-10, our approach achieves impressive results for both clean and robust accuracy under PGD-20 (epsilon = 0.031), outperforming standard adversarial training methods. Our results indicate that combining adversarial guidance with hard-mined contrastive supervision helps models learn more structured and robust representations, narrowing the gap between accuracy and robustness.

