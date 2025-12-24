---
layout: default
title: "OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing"
---

# OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08706" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08706v2</a>
  <a href="https://arxiv.org/pdf/2508.08706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08706v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08706v2', 'OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengxue Cheng, Yiqian Zhang, Wenkang Zhang, Haoyu Li, Keyu Wang, Li Song, Hengdi Zhang

**分类**: cs.RO

**发布日期**: 2025-08-12 (更新: 2025-08-22)

**备注**: 15 pages, 7 figures, 8 tables. ObjTac dataset: https://readerek.github.io/Objtac.github.io

**🔗 代码/项目**: [PROJECT_PAGE](https://readerek.github.io/Objtac.github.io)

---

## 💡 一句话要点

**提出OmniVTLA以解决触觉感知在机器人操作中的不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `触觉感知` `机器人操作` `多模态融合` `数据集构建`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在触觉感知方面严重不足，导致在接触丰富的任务中表现不佳。
2. 提出OmniVTLA架构，结合双路径触觉编码器和ObjTac数据集，提升触觉感知能力。
3. 实验结果显示，OmniVTLA在抓取任务中成功率提高至96.9%，比基线高出21.9%。

## 📝 摘要（中文）

近年来，基于视觉-语言-动作（VLA）模型的研究取得了显著进展，但现有模型在触觉感知方面存在不足，尤其是在接触丰富的任务中。为了解决这一问题，本文提出了OmniVTLA，一个结合触觉感知的创新架构。其主要贡献包括：构建了双路径触觉编码器框架，增强了不同类型触觉传感器的感知能力；引入了ObjTac数据集，涵盖56种物体的文本、视觉和触觉信息；训练了一个语义对齐的触觉编码器，提升了OmniVTLA的初始化效果。实验结果表明，OmniVTLA在抓取和放置任务中显著提高了成功率和任务完成效率。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作（VLA）模型在触觉感知方面存在显著不足，尤其是在需要精确接触的任务中，导致其性能受到限制。触觉传感器的异质性和数据获取的困难使得现有模型无法有效利用触觉信息。

**核心思路**：本文提出OmniVTLA，通过引入双路径触觉编码器框架，结合视觉和触觉信息，提升机器人在复杂操作中的感知能力。通过训练一个语义对齐的触觉编码器，OmniVTLA能够更好地整合多模态信息。

**技术框架**：OmniVTLA的整体架构包括两个主要模块：一个是预训练的视觉变换器（ViT），用于处理视觉信息；另一个是语义对齐的触觉ViT（SA-ViT），用于处理触觉信息。这两个模块通过双路径结构进行信息融合。

**关键创新**：OmniVTLA的主要创新在于其双路径触觉编码器框架，能够有效整合来自不同类型触觉传感器的信息，并通过ObjTac数据集的支持，提升了触觉感知的准确性和有效性。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态信息的融合效果，同时在触觉编码器的训练过程中，利用了ObjTac数据集中的丰富样本，确保了模型的泛化能力和适应性。

## 📊 实验亮点

实验结果显示，OmniVTLA在抓取任务中成功率达到96.9%，比现有基线提高21.9%；在灵巧手操作中成功率达到100%，比基线提高6.2%。此外，OmniVTLA在任务完成时间和轨迹平滑性方面也显著优于现有VLA模型。

## 🎯 应用场景

OmniVTLA的研究成果在机器人操作、自动化制造和人机交互等领域具有广泛的应用潜力。通过提升触觉感知能力，机器人能够更精准地执行复杂的操作任务，进而提高工作效率和安全性。未来，随着触觉传感器技术的发展，OmniVTLA有望在更多实际场景中发挥重要作用。

## 📄 摘要（原文）

> Recent vision-language-action (VLA) models build upon vision-language foundations, and have achieved promising results and exhibit the possibility of task generalization in robot manipulation. However, due to the heterogeneity of tactile sensors and the difficulty of acquiring tactile data, current VLA models significantly overlook the importance of tactile perception and fail in contact-rich tasks. To address this issue, this paper proposes OmniVTLA, a novel architecture involving tactile sensing. Specifically, our contributions are threefold. First, our OmniVTLA features a dual-path tactile encoder framework. This framework enhances tactile perception across diverse vision-based and force-based tactile sensors by using a pretrained vision transformer (ViT) and a semantically-aligned tactile ViT (SA-ViT). Second, we introduce ObjTac, a comprehensive force-based tactile dataset capturing textual, visual, and tactile information for 56 objects across 10 categories. With 135K tri-modal samples, ObjTac supplements existing visuo-tactile datasets. Third, leveraging this dataset, we train a semantically-aligned tactile encoder to learn a unified tactile representation, serving as a better initialization for OmniVTLA. Real-world experiments demonstrate substantial improvements over state-of-the-art VLA baselines, achieving 96.9% success rates with grippers, (21.9% higher over baseline) and 100% success rates with dexterous hands (6.2% higher over baseline) in pick-and-place tasks. Besides, OmniVTLA significantly reduces task completion time and generates smoother trajectories through tactile sensing compared to existing VLA. Our ObjTac dataset can be found at https://readerek.github.io/Objtac.github.io

