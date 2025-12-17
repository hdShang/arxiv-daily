---
layout: default
title: StretchySnake: Flexible SSM Training Unlocks Action Recognition Across Spatio-Temporal Scales
---

# StretchySnake: Flexible SSM Training Unlocks Action Recognition Across Spatio-Temporal Scales

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16209" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16209v1</a>
  <a href="https://arxiv.org/pdf/2510.16209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16209v1" onclick="toggleFavorite(this, '2510.16209v1', 'StretchySnake: Flexible SSM Training Unlocks Action Recognition Across Spatio-Temporal Scales')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nyle Siddiqui, Rohit Gupta, Sirnam Swetha, Mubarak Shah

**分类**: cs.CV

**发布日期**: 2025-10-17

---

## 💡 一句话要点

**StretchySnake：灵活的SSM训练解锁跨时空尺度的动作识别**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `状态空间模型` `动作识别` `视频理解` `时空尺度` `灵活训练` `长视频理解` `分辨率无关`

## 📋 核心要点

1. 现有视频理解模型，特别是基于Transformer的模型，在训练时通常采用固定分辨率和视频长度，导致模型在处理不同时空尺度的视频时性能下降。
2. 论文提出StretchySnake，一种灵活的SSM训练方法，通过在训练期间采样不同时空分辨率的视频，并动态插值模型权重，使模型适应各种时空尺度。
3. 实验结果表明，StretchySnake在短动作和长动作识别基准测试中均优于Transformer和SSM基线，性能提升高达28%，并对细粒度动作具有很强的适应性。

## 📝 摘要（中文）

状态空间模型（SSM）已成为各种任务中Transformer的一种有竞争力的替代方案。其线性复杂度和隐状态递归使其特别适合建模长序列，而注意力机制的计算成本则呈二次方增长。然而，目前用于视频理解的训练方法是为Transformer量身定制的，未能充分利用SSM的独特属性。例如，视频模型通常在固定的分辨率和视频长度下进行训练，以平衡注意力成本的二次方缩放与性能。因此，这些模型在评估具有训练期间未见过的空间和时间分辨率的视频时，性能会下降；我们称之为时空不灵活性。在动作识别的背景下，这严重限制了模型在短视频和长视频中保持性能的能力。因此，我们提出了一种灵活的训练方法，该方法利用并改进了SSM固有的适应性。我们的方法在训练期间以不同的时间和空间分辨率对视频进行采样，并动态插值模型权重以适应任何时空尺度。这使我们的SSM（我们称之为StretchySnake）具有时空灵活性，并使其能够无缝处理从短的、细粒度的剪辑到长的、复杂的活动的视频。我们介绍并比较了五种不同的灵活训练变体，并确定了视频SSM最有效的策略。在短动作（UCF-101、HMDB-51）和长动作（COIN、Breakfast）基准测试中，StretchySnake的性能优于Transformer和SSM基线，提升高达28%，并且对细粒度动作（SSV2、Diving-48）具有很强的适应性。因此，我们的方法提供了一种简单的即插即用训练方案，使视频SSM在各种动作识别场景中更加鲁棒、分辨率无关且高效。

## 🔬 方法详解

**问题定义**：现有视频动作识别模型，特别是基于Transformer的模型，由于注意力机制的二次方复杂度，通常需要在固定的时空分辨率下进行训练。这导致模型在处理与训练数据具有不同时空尺度的视频时，性能显著下降，即“时空不灵活性”问题。现有方法难以兼顾长视频和短视频的识别精度。

**核心思路**：论文的核心思路是利用SSM的线性复杂度和隐状态递归特性，并结合一种灵活的训练方法，使模型能够适应不同的时空尺度。通过在训练过程中随机采样不同分辨率和长度的视频片段，并动态调整模型权重，从而提高模型的泛化能力和鲁棒性。

**技术框架**：StretchySnake的整体框架基于状态空间模型（SSM）。训练过程包含以下主要阶段：1) 视频数据采样：从训练集中随机采样不同时空分辨率的视频片段。2) 模型权重插值：根据采样的时空分辨率，动态插值SSM的权重参数。3) 模型训练：使用采样的数据和插值后的权重训练SSM模型。4) 模型评估：在不同时空尺度的测试集上评估模型的性能。

**关键创新**：论文的关键创新在于提出了一种灵活的SSM训练方法，该方法通过动态调整模型权重，使模型能够适应不同的时空尺度。这种方法克服了传统视频模型在固定分辨率下训练的局限性，提高了模型的泛化能力和鲁棒性。与现有方法相比，StretchySnake无需对输入视频进行预处理或后处理，即可直接处理不同时空尺度的视频。

**关键设计**：论文提出了五种不同的灵活训练变体，并比较了它们的性能。关键设计包括：1) 采样策略：如何选择不同时空分辨率的视频片段。2) 权重插值方法：如何根据采样的时空分辨率动态插值模型权重。3) 损失函数：如何设计损失函数以优化模型的性能。具体参数设置和网络结构细节在论文中有详细描述，例如，采用了特定的SSM架构和优化算法。

## 📊 实验亮点

StretchySnake在多个动作识别基准测试中取得了显著的性能提升。在短动作识别数据集UCF-101和HMDB-51上，StretchySnake的性能优于Transformer和SSM基线。在长动作识别数据集COIN和Breakfast上，StretchySnake的性能提升高达28%。此外，StretchySnake在细粒度动作识别数据集SSV2和Diving-48上也表现出很强的适应性，证明了其在不同时空尺度下的泛化能力。

## 🎯 应用场景

StretchySnake具有广泛的应用前景，可用于各种需要处理不同时空尺度视频的场景，例如：视频监控、自动驾驶、体育赛事分析、医疗影像分析等。该方法可以提高视频分析系统的鲁棒性和准确性，使其能够更好地适应真实世界的复杂环境。未来，该方法可以与其他技术相结合，例如多模态融合、知识图谱等，以实现更高级的视频理解任务。

## 📄 摘要（原文）

> State space models (SSMs) have emerged as a competitive alternative to transformers in various tasks. Their linear complexity and hidden-state recurrence make them particularly attractive for modeling long sequences, whereas attention becomes quadratically expensive. However, current training methods for video understanding are tailored towards transformers and fail to fully leverage the unique attributes of SSMs. For example, video models are often trained at a fixed resolution and video length to balance the quadratic scaling of attention cost against performance. Consequently, these models suffer from degraded performance when evaluated on videos with spatial and temporal resolutions unseen during training; a property we call spatio-temporal inflexibility. In the context of action recognition, this severely limits a model's ability to retain performance across both short- and long-form videos. Therefore, we propose a flexible training method that leverages and improves the inherent adaptability of SSMs. Our method samples videos at varying temporal and spatial resolutions during training and dynamically interpolates model weights to accommodate any spatio-temporal scale. This instills our SSM, which we call StretchySnake, with spatio-temporal flexibility and enables it to seamlessly handle videos ranging from short, fine-grained clips to long, complex activities. We introduce and compare five different variants of flexible training, and identify the most effective strategy for video SSMs. On short-action (UCF-101, HMDB-51) and long-action (COIN, Breakfast) benchmarks, StretchySnake outperforms transformer and SSM baselines alike by up to 28%, with strong adaptability to fine-grained actions (SSV2, Diving-48). Therefore, our method provides a simple drop-in training recipe that makes video SSMs more robust, resolution-agnostic, and efficient across diverse action recognition scenarios.

