---
layout: default
title: "Toward Automated Regulatory Decision-Making: Trustworthy Medical Device Risk Classification with Multimodal Transformers and Self-Training"
---

# Toward Automated Regulatory Decision-Making: Trustworthy Medical Device Risk Classification with Multimodal Transformers and Self-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00422" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00422v1</a>
  <a href="https://arxiv.org/pdf/2505.00422.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00422v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00422v1', 'Toward Automated Regulatory Decision-Making: Trustworthy Medical Device Risk Classification with Multimodal Transformers and Self-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Han, Aaron Ceross, Jeroen H. M. Bergmann

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出多模态Transformer框架以解决医疗设备风险分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗设备` `风险分类` `多模态融合` `Transformer` `自训练` `交叉注意机制` `机器学习` `监管技术`

## 📋 核心要点

1. 现有的医疗设备风险分类方法往往依赖单一模态，导致分类准确性不足，难以满足监管需求。
2. 本文提出的多模态Transformer框架通过结合文本和视觉信息，利用交叉注意机制和自训练策略来提升分类性能。
3. 实验结果显示，该方法在真实数据集上取得了90.4%的准确率和97.9%的AUROC，显著优于传统的单模态方法。

## 📝 摘要（中文）

准确的医疗设备风险等级分类对于监管监督和临床安全至关重要。本文提出了一种基于Transformer的多模态框架，结合文本描述和视觉信息来预测设备的监管分类。该模型采用交叉注意机制以捕捉跨模态依赖，并使用自训练策略以在有限监督下提高泛化能力。在真实世界的监管数据集上的实验表明，该方法的准确率高达90.4%，AUROC达到97.9%，显著优于仅使用文本（77.2%）和仅使用图像（54.8%）的基线。与标准的多模态融合相比，自训练机制使SVM的准确率提高了3.3个百分点（从87.1%提升至90.4%），宏F1值提高了1.4点，表明伪标签能够有效增强有限监督下的泛化能力。消融研究进一步确认了交叉模态注意和自训练的互补效益。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗设备风险分类中的准确性不足问题。现有方法通常依赖单一模态，导致信息利用不充分，影响分类结果的可靠性。

**核心思路**：论文提出了一种多模态Transformer框架，结合文本和图像信息，通过交叉注意机制捕捉不同模态之间的依赖关系，同时采用自训练策略以增强模型在有限监督下的泛化能力。

**技术框架**：该框架主要包括数据预处理、特征提取、交叉注意机制和自训练模块。数据预处理阶段将文本和图像信息进行标准化，特征提取阶段利用Transformer模型提取深层特征，交叉注意机制用于融合不同模态的信息，自训练模块则通过伪标签提升模型的学习效果。

**关键创新**：最重要的技术创新在于引入了交叉注意机制和自训练策略的结合，这一设计使得模型能够有效捕捉模态间的相互关系，并在有限标注数据下仍能实现高效学习。

**关键设计**：模型采用了多层Transformer结构，损失函数设计为交叉熵损失，并在自训练阶段使用伪标签进行迭代更新，确保模型在训练过程中的稳定性和准确性。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，提出的方法在真实世界的监管数据集上实现了90.4%的准确率和97.9%的AUROC，分别比文本单模态（77.2%）和图像单模态（54.8%）显著提升。此外，自训练机制使得SVM的准确率提升了3.3个百分点，宏F1值提升了1.4点，验证了伪标签在有限监督下的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗设备监管、临床决策支持和智能医疗系统。通过提高医疗设备风险分类的准确性，能够有效保障患者安全，促进医疗行业的合规性和效率。未来，该技术有望扩展到其他领域的风险评估和决策支持系统中。

## 📄 摘要（原文）

> Accurate classification of medical device risk levels is essential for regulatory oversight and clinical safety. We present a Transformer-based multimodal framework that integrates textual descriptions and visual information to predict device regulatory classification. The model incorporates a cross-attention mechanism to capture intermodal dependencies and employs a self-training strategy for improved generalization under limited supervision. Experiments on a real-world regulatory dataset demonstrate that our approach achieves up to 90.4% accuracy and 97.9% AUROC, significantly outperforming text-only (77.2%) and image-only (54.8%) baselines. Compared to standard multimodal fusion, the self-training mechanism improved SVM performance by 3.3 percentage points in accuracy (from 87.1% to 90.4%) and 1.4 points in macro-F1, suggesting that pseudo-labeling can effectively enhance generalization under limited supervision. Ablation studies further confirm the complementary benefits of both cross-modal attention and self-training.

