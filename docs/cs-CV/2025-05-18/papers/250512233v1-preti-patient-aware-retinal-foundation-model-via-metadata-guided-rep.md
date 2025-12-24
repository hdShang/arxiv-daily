---
layout: default
title: PRETI: Patient-Aware Retinal Foundation Model via Metadata-Guided Representation Learning
---

# PRETI: Patient-Aware Retinal Foundation Model via Metadata-Guided Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12233" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12233v1</a>
  <a href="https://arxiv.org/pdf/2505.12233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12233v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12233v1', 'PRETI: Patient-Aware Retinal Foundation Model via Metadata-Guided Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yeonkyung Lee, Woojung Han, Youngjun Jun, Hyeonmin Kim, Jungkyung Cho, Seong Jae Hwang

**分类**: eess.IV, cs.CV

**发布日期**: 2025-05-18

**备注**: MICCAI2025 early accept

**🔗 代码/项目**: [GITHUB](https://github.com/MICV-yonsei/PRETI)

---

## 💡 一句话要点

**提出PRETI以解决视网膜图像分析中的数据依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜图像分析` `自监督学习` `元数据感知` `疾病预测` `深度学习` `医学影像` `模型鲁棒性`

## 📋 核心要点

1. 现有方法在视网膜图像分析中依赖昂贵的临床报告，限制了其应用和推广。
2. PRETI模型通过结合元数据感知学习与自监督学习，动态优化元数据表示，提升模型性能。
3. 实验表明，PRETI在多种疾病和生物标志物预测中实现了最先进的结果，显示出其强大的应用潜力。

## 📝 摘要（中文）

视网膜基础模型通过自监督学习显著提升了视网膜图像分析的能力，减少了对标注数据的依赖。然而，获取临床报告的成本高且困难。相较之下，元数据（如年龄、性别）广泛可用，能有效分析疾病进展。为此，本文提出PRETI模型，结合元数据感知学习与自监督表示学习，动态优化元数据表示，并构建患者级数据对以增强模型的鲁棒性。此外，提出的视网膜感知自适应掩蔽（RAAM）策略在训练过程中动态调整掩蔽比例，提升了图像表示的效果。实验结果表明，PRETI在多种疾病和生物标志物预测中均达到了最先进的性能，强调了元数据引导的基础模型在视网膜疾病分析中的重要性。

## 🔬 方法详解

**问题定义**：当前视网膜图像分析方法过于依赖标注数据，尤其是临床报告，获取成本高且困难，限制了模型的广泛应用。

**核心思路**：PRETI模型通过引入元数据（如年龄、性别）来增强模型的学习能力，结合自监督学习减少对标注数据的依赖，提升模型的泛化能力。

**技术框架**：PRETI的整体架构包括元数据感知学习模块、可学习的元数据嵌入（LME）和视网膜感知自适应掩蔽（RAAM）策略，构建患者级数据对以提高鲁棒性。

**关键创新**：PRETI的核心创新在于动态优化元数据表示和自适应掩蔽策略，能够在训练过程中根据视网膜区域的特征调整掩蔽比例，从而更好地捕捉图像中的病理细节。

**关键设计**：模型设计中，LME模块用于动态调整元数据的表示，RAAM策略则在训练过程中根据视网膜区域的特征动态调整掩蔽比例，确保模型能够有效学习到全局结构和细粒度病理信息。实验中使用了多种损失函数和网络结构，以确保模型的鲁棒性和准确性。

## 📊 实验亮点

PRETI在多种疾病和生物标志物预测中表现出色，实验结果显示其在准确率和鲁棒性上均超越了现有的最先进方法，具体性能提升幅度达到XX%（具体数据待补充），验证了元数据引导的基础模型在视网膜疾病分析中的重要性。

## 🎯 应用场景

PRETI模型在视网膜疾病分析中具有广泛的应用潜力，能够帮助医生更准确地进行疾病诊断和进展评估。通过利用易获取的元数据，模型可以在临床实践中降低对昂贵标注数据的依赖，提升医疗服务的效率和可及性。未来，该模型还可以扩展到其他医学影像分析领域，推动智能医疗的发展。

## 📄 摘要（原文）

> Retinal foundation models have significantly advanced retinal image analysis by leveraging self-supervised learning to reduce dependence on labeled data while achieving strong generalization. Many recent approaches enhance retinal image understanding using report supervision, but obtaining clinical reports is often costly and challenging. In contrast, metadata (e.g., age, gender) is widely available and serves as a valuable resource for analyzing disease progression. To effectively incorporate patient-specific information, we propose PRETI, a retinal foundation model that integrates metadata-aware learning with robust self-supervised representation learning. We introduce Learnable Metadata Embedding (LME), which dynamically refines metadata representations. Additionally, we construct patient-level data pairs, associating images from the same individual to improve robustness against non-clinical variations. To further optimize retinal image representation, we propose Retina-Aware Adaptive Masking (RAAM), a strategy that selectively applies masking within the retinal region and dynamically adjusts the masking ratio during training. PRETI captures both global structures and fine-grained pathological details, resulting in superior diagnostic performance. Extensive experiments demonstrate that PRETI achieves state-of-the-art results across diverse diseases and biomarker predictions using in-house and public data, indicating the importance of metadata-guided foundation models in retinal disease analysis. Our code and pretrained model are available at https://github.com/MICV-yonsei/PRETI

