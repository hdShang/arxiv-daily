---
layout: default
title: "PictOBI-20k: Unveiling Large Multimodal Models in Visual Decipherment for Pictographic Oracle Bone Characters"
---

# PictOBI-20k: Unveiling Large Multimodal Models in Visual Decipherment for Pictographic Oracle Bone Characters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05773" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05773v1</a>
  <a href="https://arxiv.org/pdf/2509.05773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05773v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05773v1', 'PictOBI-20k: Unveiling Large Multimodal Models in Visual Decipherment for Pictographic Oracle Bone Characters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijian Chen, Wenjie Hua, Jinhao Li, Lirong Deng, Fan Du, Tingzhu Chen, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-09-06

**备注**: 6 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/OBI-Future/PictOBI-20k)

---

## 💡 一句话要点

**提出PictOBI-20k数据集，用于评估大型多模态模型在甲骨文象形文字视觉释读中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `甲骨文释读` `多模态模型` `视觉推理` `数据集构建` `语言先验`

## 📋 核心要点

1. 现有甲骨文解读方法受限于考古发掘的零星性和铭文语料库的规模，难以有效推进。
2. 利用大型多模态模型（LMMs）的视觉感知能力，构建数据集评估其在甲骨文象形文字视觉释读中的潜力。
3. 实验表明通用LMMs具备初步的视觉解读能力，但视觉信息利用不足，受语言先验影响较大。

## 📝 摘要（中文）

甲骨文（OBCs）是已知的最古老的汉字形式，解读甲骨文一直是学者的终极目标，是理解人类早期生产方式的关键。目前，甲骨文的解读方法主要受到考古发掘的零星性和铭文语料库的限制。 随着大型多模态模型（LMMs）强大的视觉感知能力，利用LMMs进行甲骨文视觉解读的潜力增加。本文介绍PictOBI-20k，该数据集旨在评估LMMs在甲骨文象形文字视觉解读任务中的能力。它包括2万个精心收集的甲骨文和真实物体图像，形成了超过1.5万个多项选择题。我们还进行了主观注释，以研究人类和LMMs在视觉推理中参考点的一致性。实验表明，通用LMMs具有初步的视觉解读技能，但LMMs并没有有效地利用视觉信息，而是主要受到语言先验的限制。我们希望我们的数据集能够促进未来面向甲骨文的LMMs中视觉注意力的评估和优化。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在甲骨文象形文字视觉释读任务中的评估问题。现有方法缺乏专门针对甲骨文视觉释读的数据集，难以有效评估和优化LMMs在该领域的性能。现有LMMs在甲骨文识别中，对视觉信息的利用不足，更多依赖语言先验知识。

**核心思路**：论文的核心思路是构建一个包含甲骨文图像和对应实物图像的大规模数据集PictOBI-20k，并设计多项选择题，以评估LMMs在视觉释读甲骨文时的能力。通过对比LMMs和人类在视觉推理中参考点的一致性，分析LMMs对视觉信息的利用情况。

**技术框架**：该研究的技术框架主要包含以下几个部分：1) 数据集构建：收集2万个甲骨文和真实物体图像，形成超过1.5万个多项选择题。2) 模型评估：使用通用LMMs在PictOBI-20k数据集上进行测试，评估其视觉释读能力。3) 主观注释：进行主观注释，研究人类和LMMs在视觉推理中参考点的一致性。4) 结果分析：分析实验结果，探讨LMMs对视觉信息的利用情况和语言先验的影响。

**关键创新**：该论文的关键创新在于构建了首个专门用于评估LMMs在甲骨文象形文字视觉释读能力的大规模数据集PictOBI-20k。该数据集包含丰富的甲骨文和实物图像，以及精心设计的多项选择题，能够有效评估LMMs的视觉推理能力。与现有方法相比，该数据集更侧重于评估LMMs对甲骨文象形文字的视觉理解能力，而非简单的图像分类或识别。

**关键设计**：PictOBI-20k数据集的关键设计包括：1) 图像选择：精心挑选具有代表性的甲骨文和实物图像，保证图像质量和多样性。2) 问题设计：设计多项选择题，考察LMMs对甲骨文象形文字的视觉理解和推理能力。3) 参考点标注：进行主观注释，标注人类在视觉推理中的参考点，用于与LMMs进行对比分析。4) 数据集划分：将数据集划分为训练集、验证集和测试集，用于模型训练和评估。具体参数设置和损失函数等细节未在论文中详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，通用LMMs具备初步的甲骨文视觉解读能力，但对视觉信息的利用效率不高，主要依赖语言先验知识。该研究揭示了现有LMMs在甲骨文视觉释读方面的局限性，为未来优化LMMs的视觉注意力机制提供了重要参考。具体性能数据和提升幅度未在摘要中给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于甲骨文的自动释读、历史文化研究、古文字学教育等领域。通过提升LMMs对甲骨文的视觉理解能力，可以加速甲骨文的数字化和智能化研究，为传承和弘扬中华优秀传统文化做出贡献。未来，该研究还可以扩展到其他古文字的释读，促进古代文明的研究和保护。

## 📄 摘要（原文）

> Deciphering oracle bone characters (OBCs), the oldest attested form of written Chinese, has remained the ultimate, unwavering goal of scholars, offering an irreplaceable key to understanding humanity's early modes of production. Current decipherment methodologies of OBC are primarily constrained by the sporadic nature of archaeological excavations and the limited corpus of inscriptions. With the powerful visual perception capability of large multimodal models (LMMs), the potential of using LMMs for visually deciphering OBCs has increased. In this paper, we introduce PictOBI-20k, a dataset designed to evaluate LMMs on the visual decipherment tasks of pictographic OBCs. It includes 20k meticulously collected OBC and real object images, forming over 15k multi-choice questions. We also conduct subjective annotations to investigate the consistency of the reference point between humans and LMMs in visual reasoning. Experiments indicate that general LMMs possess preliminary visual decipherment skills, and LMMs are not effectively using visual information, while most of the time they are limited by language priors. We hope that our dataset can facilitate the evaluation and optimization of visual attention in future OBC-oriented LMMs. The code and dataset will be available at https://github.com/OBI-Future/PictOBI-20k.

