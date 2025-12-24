---
layout: default
title: "Human Empathy as Encoder: AI-Assisted Depression Assessment in Special Education"
---

# Human Empathy as Encoder: AI-Assisted Depression Assessment in Special Education

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23631" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23631v3</a>
  <a href="https://arxiv.org/pdf/2505.23631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23631v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23631v3', 'Human Empathy as Encoder: AI-Assisted Depression Assessment in Special Education')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boning Zhao, Xinnuo Li, Yutong Hu

**分类**: cs.HC, cs.AI, cs.CL

**发布日期**: 2025-05-29 (更新: 2025-10-05)

**备注**: 7 pages, 6 figures, ACII 2025

---

## 💡 一句话要点

**提出人类同理心编码器以解决特殊教育中的抑郁评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类同理心` `抑郁评估` `特殊教育` `多模态融合` `情感计算` `AI框架` `教师洞察`

## 📋 核心要点

1. 现有的抑郁评估方法在特殊教育环境中面临挑战，标准化问卷无法全面反映学生的真实情况。
2. 本文提出人类同理心编码器（HEAE），通过将教师的同理心洞察与学生叙述文本结合，提升抑郁评估的准确性。
3. 实验结果显示，该方法在7级抑郁严重性分类中达到了82.74%的准确率，显著提高了评估效果。

## 📝 摘要（中文）

在特殊教育环境中评估学生抑郁症是一项挑战。标准化问卷可能无法全面反映学生的真实情况，而自动化方法在处理丰富的学生叙述时往往缺乏教师与学生之间同理心连接所带来的个性化洞察。为了解决这些局限性，本文提出了一种名为人类同理心编码器（HEAE）的新型人本AI框架，旨在实现透明和社会责任感的抑郁严重性评估。该方法将学生叙述文本与教师衍生的9维“同理心向量”相结合，明确将隐性同理心洞察转化为结构化的AI输入，从而增强而非替代人类判断。通过严格的实验优化多模态融合、文本表示和分类架构，实现了82.74%的7级严重性分类准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决在特殊教育环境中评估学生抑郁症的困难，现有方法往往无法有效整合教师的同理心理解，导致评估结果的模糊性和不准确性。

**核心思路**：论文提出的人类同理心编码器（HEAE）通过将教师的同理心洞察转化为结构化的AI输入，旨在增强抑郁评估的准确性和个性化，促进人机协作。

**技术框架**：HEAE框架包括多个模块，首先是学生叙述文本的处理，其次是构建9维同理心向量（EV），最后通过多模态融合和分类架构进行抑郁严重性评估。

**关键创新**：HEAE的核心创新在于将教师的同理心转化为可量化的同理心向量，并与学生的叙述文本结合，形成一种新的评估方式，显著区别于传统的问卷和自动化评估方法。

**关键设计**：在设计中，使用了PHQ-9框架指导同理心向量的构建，优化了多模态融合和文本表示的网络结构，确保了分类准确率的提升。实验中实现了82.74%的准确率，表明该方法的有效性。

## 📊 实验亮点

实验结果表明，HEAE在7级抑郁严重性分类中达到了82.74%的准确率，显著高于传统方法。这一成果展示了通过人类同理心的结构化嵌入，能够有效提升抑郁评估的准确性和个性化水平。

## 🎯 应用场景

该研究的潜在应用领域包括特殊教育、心理健康评估和教育技术等。通过将人类同理心与AI技术结合，可以为教育工作者提供更为精准的学生心理状态评估工具，促进学生的心理健康发展。未来，该方法可能在更广泛的心理健康领域中发挥重要作用，推动人机协作的深入发展。

## 📄 摘要（原文）

> Assessing student depression in sensitive environments like special education is challenging. Standardized questionnaires may not fully reflect students' true situations. Furthermore, automated methods often falter with rich student narratives, lacking the crucial, individualized insights stemming from teachers' empathetic connections with students. Existing methods often fail to address this ambiguity or effectively integrate educator understanding. To address these limitations by fostering a synergistic human-AI collaboration, this paper introduces Human Empathy as Encoder (HEAE), a novel, human-centered AI framework for transparent and socially responsible depression severity assessment. Our approach uniquely integrates student narrative text with a teacher-derived, 9-dimensional "Empathy Vector" (EV), its dimensions guided by the PHQ-9 framework,to explicitly translate tacit empathetic insight into a structured AI input enhancing rather than replacing human judgment. Rigorous experiments optimized the multimodal fusion, text representation, and classification architecture, achieving 82.74% accuracy for 7-level severity classification. This work demonstrates a path toward more responsible and ethical affective computing by structurally embedding human empathy

