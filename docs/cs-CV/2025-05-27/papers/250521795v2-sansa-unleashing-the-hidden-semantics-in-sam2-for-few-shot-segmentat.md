---
layout: default
title: "SANSA: Unleashing the Hidden Semantics in SAM2 for Few-Shot Segmentation"
---

# SANSA: Unleashing the Hidden Semantics in SAM2 for Few-Shot Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21795" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21795v2</a>
  <a href="https://arxiv.org/pdf/2505.21795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21795v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21795v2', 'SANSA: Unleashing the Hidden Semantics in SAM2 for Few-Shot Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Claudia Cuttano, Gabriele Trivigno, Giuseppe Averta, Carlo Masone

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-11-15)

**备注**: Accepted to NeurIPS 2025 as Spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/ClaudiaCuttano/SANSA)

---

## 💡 一句话要点

**提出SANSA以解决少样本分割中的语义理解问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `少样本分割` `语义理解` `特征提取` `深度学习` `模型优化`

## 📋 核心要点

1. 现有方法在少样本分割中面临语义理解不足的问题，尤其是SAM2的表示与任务特定线索纠缠，限制了其应用。
2. 论文提出SANSA框架，通过显性化SAM2的潜在语义结构，最小化任务特定修改，从而提升少样本分割性能。
3. SANSA在少样本分割基准测试中表现出色，超越了现有通用方法，支持多种交互方式，并显著提高了处理速度和紧凑性。

## 📝 摘要（中文）

少样本分割旨在从少量标注示例中分割未见物体类别。这需要能够识别图像中语义相关物体的机制，并准确生成分割掩码。尽管Segment Anything 2（SAM2）具有强大的分割能力和内置特征匹配过程，但其表示与针对物体跟踪优化的任务特定线索纠缠在一起，影响了其在需要更高语义理解的任务中的使用。我们提出SANSA（语义对齐的Segment Anything 2），通过最小的任务特定修改，使SAM2的潜在结构显性化，并重新用于少样本分割。SANSA在专门设计的少样本分割基准上实现了最先进的性能，超越了流行的上下文设置中的通用方法，支持通过点、框或涂鸦的灵活交互，并且比之前的方法显著更快和更紧凑。

## 🔬 方法详解

**问题定义**：本论文旨在解决少样本分割任务中的语义理解不足问题。现有方法如SAM2的表示受到任务特定线索的影响，限制了其在更高层次语义理解任务中的有效性。

**核心思路**：论文的核心思路是通过显性化SAM2中潜在的语义结构，重新调整其用于少样本分割的能力。尽管SAM2经过无类预训练，但其特征中已经编码了丰富的语义信息。

**技术框架**：SANSA框架主要包括两个模块：首先是对SAM2特征的提取与处理，其次是通过最小化任务特定修改来实现少样本分割。整体流程是先利用SAM2进行初步分割，然后通过SANSA对结果进行优化。

**关键创新**：最重要的技术创新在于将SAM2的潜在语义结构显性化，并通过简单的修改使其适应少样本分割任务。这一方法与现有方法的本质区别在于，前者利用了SAM2的强大特征提取能力，而后者往往依赖于复杂的任务特定设计。

**关键设计**：在关键设计方面，SANSA采用了灵活的交互方式，包括点、框和涂鸦等输入形式，此外，损失函数和网络结构经过优化，以确保在少样本分割任务中的高效性和准确性。整体架构保持了SAM2的优势，同时增强了其在特定任务中的表现。

## 📊 实验亮点

SANSA在少样本分割基准测试中实现了最先进的性能，超越了现有的通用方法，特别是在流行的上下文设置中表现突出。具体而言，SANSA在多个评估指标上均显示出显著提升，处理速度和模型紧凑性也优于以往方法，展现了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、医学影像分析和机器人视觉等。通过提升少样本分割的能力，SANSA能够在数据稀缺的情况下，快速适应新任务，具有重要的实际价值和广泛的应用前景。未来，随着更多领域对少样本学习的需求增加，SANSA的影响力将进一步扩大。

## 📄 摘要（原文）

> Few-shot segmentation aims to segment unseen object categories from just a handful of annotated examples. This requires mechanisms that can both identify semantically related objects across images and accurately produce segmentation masks. We note that Segment Anything 2 (SAM2), with its prompt-and-propagate mechanism, offers both strong segmentation capabilities and a built-in feature matching process. However, we show that its representations are entangled with task-specific cues optimized for object tracking, which impairs its use for tasks requiring higher level semantic understanding. Our key insight is that, despite its class-agnostic pretraining, SAM2 already encodes rich semantic structure in its features. We propose SANSA (Semantically AligNed Segment Anything 2), a framework that makes this latent structure explicit, and repurposes SAM2 for few-shot segmentation through minimal task-specific modifications. SANSA achieves state-of-the-art performance on few-shot segmentation benchmarks specifically designed to assess generalization, outperforms generalist methods in the popular in-context setting, supports various prompts flexible interaction via points, boxes, or scribbles, and remains significantly faster and more compact than prior approaches. Code is available at https://github.com/ClaudiaCuttano/SANSA.

