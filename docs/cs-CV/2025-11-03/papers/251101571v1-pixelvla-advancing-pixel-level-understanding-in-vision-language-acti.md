---
layout: default
title: "PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model"
---

# PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01571" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01571v1</a>
  <a href="https://arxiv.org/pdf/2511.01571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01571v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.01571v1', 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqi Liang, Gan Sun, Yao He, Jiahua Dong, Suyan Dai, Ivan Laptev, Salman Khan, Yang Cong

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-03

**备注**: 17pages,7 figures, 5 tabels

---

## 💡 一句话要点

**PixelVLA：通过像素级理解和多模态提示，提升视觉-语言-动作模型的性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉-语言-动作模型` `像素级理解` `多模态提示` `机器人控制` `视觉运动指令调优`

## 📋 核心要点

1. 现有VLA模型在像素级场景理解方面存在不足，且过度依赖文本提示，限制了其在真实场景中的应用。
2. PixelVLA通过引入多尺度像素感知编码器和视觉提示编码器，支持像素级推理和多模态提示。
3. 实验表明，PixelVLA在操纵成功率上显著优于现有模型，且训练成本更低，证明了其有效性。

## 📝 摘要（中文）

视觉-语言-动作模型(VLA)正成为学习通用视觉运动控制策略的强大工具。然而，当前的VLA主要在大型图像-文本-动作数据上训练，并在两个关键方面受到限制：(i)它们难以进行像素级场景理解，以及(ii)它们严重依赖文本提示，这降低了它们在现实环境中的灵活性。为了应对这些挑战，我们引入了PixelVLA，这是第一个旨在支持像素级推理和文本与视觉输入的多模态提示的VLA模型。我们的方法建立在一个新的视觉运动指令调优框架之上，该框架集成了多尺度像素感知编码器和视觉提示编码器。为了有效地训练PixelVLA，我们进一步提出了一个两阶段自动标注流程，生成了Pixel-160K，这是一个从现有机器人数据中提取的具有像素级标注的大规模数据集。在三个标准VLA基准和两个VLA模型变体上的实验表明，PixelVLA比OpenVLA的操纵成功率提高了10.1%-17.8%，而仅需其1.5%的预训练成本。这些结果表明，PixelVLA可以集成到现有的VLA中，从而在复杂的环境中实现更准确、高效和通用的机器人控制。数据集和代码将开源发布。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作模型（VLA）难以进行像素级别的场景理解，并且过度依赖文本提示，这限制了它们在复杂和真实的机器人控制任务中的应用。现有的VLA模型通常只关注全局图像特征和文本指令，忽略了图像中特定像素区域的重要性，导致无法精确地执行需要细粒度感知的任务。

**核心思路**：PixelVLA的核心思路是通过引入像素级的信息处理能力，增强VLA模型对场景的理解。同时，模型支持多模态的提示方式，包括文本和视觉输入，从而提高模型的灵活性和适应性。通过这种方式，模型可以更好地理解用户的意图，并精确地执行相应的动作。

**技术框架**：PixelVLA的整体框架包含以下几个主要模块：1) 多尺度像素感知编码器：用于提取图像的像素级特征，并融合不同尺度的信息。2) 视觉提示编码器：用于处理视觉提示信息，例如目标物体的图像区域。3) 指令调优框架：将像素级特征、视觉提示和文本指令进行融合，并生成相应的动作指令。该框架采用两阶段自动标注流程，生成大规模像素级标注数据集Pixel-160K。

**关键创新**：PixelVLA的关键创新在于其像素级理解能力和多模态提示机制。与传统的VLA模型相比，PixelVLA能够更精确地理解场景中的细节信息，并根据用户的视觉提示进行更灵活的控制。此外，Pixel-160K数据集的构建也为像素级VLA模型的训练提供了重要的数据支持。

**关键设计**：PixelVLA采用了多尺度卷积神经网络来提取像素级特征，并使用注意力机制来融合不同尺度的信息。视觉提示编码器使用Transformer结构来处理视觉提示信息。损失函数包括动作预测损失和像素级理解损失，以确保模型能够准确地预测动作并理解场景。

## 📊 实验亮点

PixelVLA在三个标准VLA基准测试中，相较于OpenVLA，操纵成功率提升了10.1%-17.8%。同时，PixelVLA仅需OpenVLA 1.5%的预训练成本，表明其具有更高的训练效率。这些结果验证了PixelVLA在提升VLA模型性能方面的有效性。

## 🎯 应用场景

PixelVLA在机器人控制、自动化装配、智能家居等领域具有广泛的应用前景。例如，它可以用于引导机器人完成精细的装配任务，或者根据用户的视觉指令控制智能家居设备。该研究的成果有助于提升机器人的智能化水平，使其能够更好地适应复杂和动态的环境。

## 📄 摘要（原文）

> Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual prompting encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-17.8% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments. The dataset and code will be released as open source.

