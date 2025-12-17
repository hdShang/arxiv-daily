---
layout: default
title: Multimodal Detection of Fake Reviews using BERT and ResNet-50
---

# Multimodal Detection of Fake Reviews using BERT and ResNet-50

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00020" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00020v1</a>
  <a href="https://arxiv.org/pdf/2511.00020.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00020v1" onclick="toggleFavorite(this, '2511.00020v1', 'Multimodal Detection of Fake Reviews using BERT and ResNet-50')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suhasnadh Reddy Veluru, Sai Teja Erukude, Viswa Chaitanya Marella

**分类**: cs.AI, cs.CL, cs.CV

**发布日期**: 2025-10-24

**备注**: Published in IEEE

**DOI**: [10.1109/ICIMIA67127.2025.11200892](https://doi.org/10.1109/ICIMIA67127.2025.11200892)

---

## 💡 一句话要点

**提出基于BERT和ResNet-50的多模态虚假评论检测方法，提升电商平台信任度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚假评论检测` `多模态学习` `BERT` `ResNet-50` `文本图像融合` `内容审核`

## 📋 核心要点

1. 现有虚假评论检测模型主要依赖单模态文本数据，忽略了跨模态语义不一致性，导致检测效果受限。
2. 提出一种多模态虚假评论检测框架，融合BERT文本特征和ResNet-50视觉特征，提升检测准确性。
3. 实验结果表明，该模型在包含21142张图像的数据集上，F1分数达到0.934，优于单模态基线。

## 📝 摘要（中文）

本文提出了一种鲁棒的多模态虚假评论检测框架，旨在解决当前数字商业环境中虚假评论泛滥的问题。该框架集成了BERT编码的文本特征和ResNet-50提取的视觉特征，通过分类头融合这些表示，联合预测评论的真实性。为了支持该方法，作者构建了一个包含21142张用户上传图像的数据集，涵盖食品配送、酒店和电子商务领域。实验结果表明，该多模态模型优于单模态基线模型，在测试集上实现了0.934的F1分数。混淆矩阵和定性分析进一步表明，该模型能够检测到细微的不一致性，例如夸张的文本赞美与不相关或低质量图像的配对，这些常见于欺骗性内容中。这项研究证明了多模态学习在维护数字信任方面的关键作用，并为各种在线平台的内容审核提供了一个可扩展的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决在线评论系统中虚假评论泛滥的问题。现有方法主要依赖于文本信息，忽略了图像信息，无法有效检测出文本与图像内容不一致的虚假评论。这些虚假评论通常由机器人、付费水军或AI模型生成，严重损害了用户信任和平台声誉。

**核心思路**：论文的核心思路是利用多模态信息融合，同时考虑评论文本和相关图像，通过捕捉文本和图像之间的语义不一致性来识别虚假评论。作者认为，真实的评论通常文本内容与图像内容是相关的，而虚假评论可能存在夸大其词的文本描述与质量低劣或不相关的图像配对。

**技术框架**：该框架主要包含两个模态的特征提取模块和一个融合分类模块。首先，使用BERT模型提取评论文本的特征向量。然后，使用ResNet-50模型提取评论图像的特征向量。最后，将两个模态的特征向量进行融合，通过一个分类头（classification head）进行二分类，判断评论是真实评论还是虚假评论。

**关键创新**：该论文的关键创新在于将多模态学习应用于虚假评论检测，并证明了图像信息对于提高检测准确性的有效性。与传统的单模态方法相比，该方法能够更好地捕捉评论中的语义不一致性，从而更准确地识别虚假评论。

**关键设计**：在文本特征提取方面，使用了预训练的BERT模型，并针对评论文本进行了微调。在图像特征提取方面，使用了预训练的ResNet-50模型，并进行了迁移学习。在融合分类模块中，使用了简单的线性层和Sigmoid激活函数进行二分类。数据集包含21142张用户上传的图像，涵盖食品配送、酒店和电子商务领域。

## 📊 实验亮点

实验结果表明，该多模态模型在虚假评论检测任务中取得了显著的性能提升，F1分数达到0.934，超过了单模态基线模型。混淆矩阵和定性分析表明，该模型能够有效识别文本与图像不一致的虚假评论，例如夸张的文本赞美与低质量图像的组合。这证明了多模态信息融合在虚假评论检测中的有效性。

## 🎯 应用场景

该研究成果可应用于电商平台、社交媒体、在线旅游平台等，用于自动检测和过滤虚假评论，提升平台内容质量和用户信任度。该技术还有助于保护商家声誉，防止恶意竞争，维护公平的商业环境。未来，该方法可以扩展到其他类型的多模态欺诈检测任务中。

## 📄 摘要（原文）

> In the current digital commerce landscape, user-generated reviews play a critical role in shaping consumer behavior, product reputation, and platform credibility. However, the proliferation of fake or misleading reviews often generated by bots, paid agents, or AI models poses a significant threat to trust and transparency within review ecosystems. Existing detection models primarily rely on unimodal, typically textual, data and therefore fail to capture semantic inconsistencies across different modalities. To address this gap, a robust multimodal fake review detection framework is proposed, integrating textual features encoded with BERT and visual features extracted using ResNet-50. These representations are fused through a classification head to jointly predict review authenticity. To support this approach, a curated dataset comprising 21,142 user-uploaded images across food delivery, hospitality, and e-commerce domains was utilized. Experimental results indicate that the multimodal model outperforms unimodal baselines, achieving an F1-score of 0.934 on the test set. Additionally, the confusion matrix and qualitative analysis highlight the model's ability to detect subtle inconsistencies, such as exaggerated textual praise paired with unrelated or low-quality images, commonly found in deceptive content. This study demonstrates the critical role of multimodal learning in safeguarding digital trust and offers a scalable solution for content moderation across various online platforms.

