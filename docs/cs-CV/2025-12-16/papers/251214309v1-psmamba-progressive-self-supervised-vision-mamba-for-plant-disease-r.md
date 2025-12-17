---
layout: default
title: PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition
---

# PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14309" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14309v1</a>
  <a href="https://arxiv.org/pdf/2512.14309.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14309v1" onclick="toggleFavorite(this, '2512.14309v1', 'PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdullah Al Mamun, Miaohua Zhang, David Ahmedt-Aristizabal, Zeeshan Hayder, Mohammad Awrangjeb

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**PSMamba：一种用于植物病害识别的渐进式自监督视觉Mamba方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `植物病害识别` `自监督学习` `Vision Mamba` `分层蒸馏` `多尺度特征学习`

## 📋 核心要点

1. 现有自监督学习方法难以捕捉植物病害图像中分层、多尺度的病变模式。
2. PSMamba采用双学生分层蒸馏策略，利用Vision Mamba进行高效序列建模，从而学习上下文和细节表征。
3. 实验表明，PSMamba在植物病害识别任务中优于现有自监督学习方法，具有更好的准确性和鲁棒性。

## 📝 摘要（中文）

自监督学习(SSL)已成为一种无需手动标注即可进行表征学习的强大范例。然而，大多数现有框架侧重于全局对齐，难以捕捉植物病害图像中具有代表性的分层、多尺度病变模式。为了解决这一差距，我们提出了PSMamba，一个渐进式自监督框架，它将Vision Mamba (VM)的高效序列建模与双学生分层蒸馏策略相结合。与传统的单教师-学生设计不同，PSMamba采用共享的全局教师和两个专门的学生：一个处理中等尺度的视图以捕捉病变分布和静脉结构，另一个专注于局部视图以捕捉纹理不规则和早期病变等细粒度线索。这种多粒度监督促进了上下文和详细表征的联合学习，一致性损失确保了连贯的跨尺度对齐。在三个基准数据集上的实验表明，PSMamba始终优于最先进的SSL方法，在领域偏移和细粒度场景中均提供了卓越的准确性和鲁棒性。

## 🔬 方法详解

**问题定义**：植物病害识别任务需要捕捉图像中不同尺度的病变特征，现有自监督学习方法侧重于全局对齐，忽略了病害图像中重要的局部细节和多尺度信息，导致识别精度受限。

**核心思路**：PSMamba的核心思路是利用双学生网络，分别学习不同尺度的特征表示，并通过一致性损失进行跨尺度对齐。全局教师网络提供整体指导，两个学生网络分别关注中等尺度和局部尺度的特征，从而实现对病害图像更全面的理解。

**技术框架**：PSMamba框架包含一个共享的全局教师网络和两个专门的学生网络。全局教师网络处理全局视图，提供整体的特征表示。一个学生网络处理中等尺度的视图，捕捉病变分布和静脉结构；另一个学生网络处理局部视图，捕捉纹理不规则和早期病变等细粒度线索。通过一致性损失，确保不同尺度的特征表示能够有效对齐。

**关键创新**：PSMamba的关键创新在于双学生分层蒸馏策略，它能够同时学习全局上下文信息和局部细节信息，从而更好地捕捉植物病害图像的多尺度特征。此外，PSMamba还采用了Vision Mamba作为骨干网络，提高了序列建模的效率。

**关键设计**：PSMamba的关键设计包括：1) 双学生网络的结构和训练方式；2) 一致性损失函数的选择和权重设置，用于约束不同尺度特征表示的一致性；3) Vision Mamba的配置，例如状态空间模型的维度和层数等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309v1/Figures/global.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309v1/Figures/psmamba.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14309v1/Figures/visual/gradcam/pd_o_2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PSMamba在三个基准植物病害数据集上进行了评估，结果表明其性能优于现有的自监督学习方法。在领域偏移场景和细粒度识别场景中，PSMamba均表现出更强的鲁棒性和准确性。具体性能数据在论文中详细展示，相较于SOTA方法有显著提升。

## 🎯 应用场景

PSMamba可应用于智慧农业领域，辅助植物病害的早期诊断和精准防治。通过分析植物叶片图像，可以快速准确地识别病害类型和程度，为农民提供及时的防治建议，减少农药使用，提高农作物产量和质量。该研究还可扩展到其他医学图像分析等领域。

## 📄 摘要（原文）

> Self-supervised Learning (SSL) has become a powerful paradigm for representation learning without manual annotations. However, most existing frameworks focus on global alignment and struggle to capture the hierarchical, multi-scale lesion patterns characteristic of plant disease imagery. To address this gap, we propose PSMamba, a progressive self-supervised framework that integrates the efficient sequence modelling of Vision Mamba (VM) with a dual-student hierarchical distillation strategy. Unlike conventional single teacher-student designs, PSMamba employs a shared global teacher and two specialised students: one processes mid-scale views to capture lesion distributions and vein structures, while the other focuses on local views to capture fine-grained cues such as texture irregularities and early-stage lesions. This multi-granular supervision facilitates the joint learning of contextual and detailed representations, with consistency losses ensuring coherent cross-scale alignment. Experiments on three benchmark datasets show that PSMamba consistently outperforms state-of-the-art SSL methods, delivering superior accuracy and robustness in both domain-shifted and fine-grained scenarios.

