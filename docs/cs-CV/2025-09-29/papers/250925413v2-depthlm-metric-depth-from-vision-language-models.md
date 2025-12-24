---
layout: default
title: "DepthLM: Metric Depth From Vision Language Models"
---

# DepthLM: Metric Depth From Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25413" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25413v2</a>
  <a href="https://arxiv.org/pdf/2509.25413.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25413v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25413v2', 'DepthLM: Metric Depth From Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhipeng Cai, Ching-Feng Yeh, Hu Xu, Zhuang Liu, Gregory Meyer, Xinjie Lei, Changsheng Zhao, Shang-Wen Li, Vikas Chandra, Yangyang Shi

**分类**: cs.CV

**发布日期**: 2025-09-29 (更新: 2025-10-01)

---

## 💡 一句话要点

**DepthLM：利用视觉语言模型实现度量深度估计，无需修改架构或损失函数。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉语言模型` `度量深度估计` `文本监督微调` `视觉提示` `内在条件增强` `三维理解` `深度学习`

## 📋 核心要点

1. 现有视觉语言模型在3D理解方面存在不足，尤其是在度量深度估计任务上，需要专门的架构和损失函数。
2. DepthLM通过文本监督微调VLM，利用视觉提示和内在条件增强解决像素参考和相机歧义问题，提升深度估计精度。
3. 实验表明，DepthLM在度量深度估计任务上超越了现有VLM，并与纯视觉模型相当，且避免了过度平滑问题。

## 📝 摘要（中文）

视觉语言模型(VLM)可以通过文本交互灵活地处理各种视觉任务。尽管在语义理解方面取得了成功，但包括GPT-5在内的最先进的VLM在理解2D输入的3D信息方面仍然存在困难。另一方面，纯视觉模型在度量深度估计这一关键的3D理解任务中达到了超人的精度。然而，它们需要特定于任务的架构和损失函数。这种差异促使我们思考：VLM是否可以在不改变架构或损失函数的情况下达到专家级的精度？我们以逐像素度量深度估计作为代表性任务，并表明答案是肯定的！令人惊讶的是，全面的分析表明，基于文本的稀疏标签监督微调足以让VLM释放强大的3D理解能力，不需要密集的预测头或复杂的回归/正则化损失。VLM的瓶颈实际上在于像素参考和跨数据集相机歧义，我们通过视觉提示和内在条件增强来解决这些问题。我们提出的DepthLM方法使用更小的模型，其精度超过了大多数先进的VLM 2倍以上，首次使VLM与纯视觉模型相媲美。有趣的是，在训练过程中没有明确强制执行的情况下，使用DepthLM训练的VLM自然地避免了过度平滑，与纯视觉模型相比，在边界区域的悬浮点要少得多。DepthLM的简单性还使单个VLM能够覆盖度量深度之外的各种3D任务。我们的代码和模型将在以下链接发布。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉语言模型（VLM）在度量深度估计任务中的不足。现有VLM虽然在语义理解方面表现出色，但在理解2D图像的3D信息，特别是精确的度量深度方面，仍然落后于专门的纯视觉模型。现有方法通常需要针对特定任务设计复杂的网络结构和损失函数，缺乏通用性和灵活性。

**核心思路**：论文的核心思路是，通过简单的文本监督微调，即可使VLM具备强大的3D理解能力，而无需修改VLM的架构或引入复杂的损失函数。关键在于解决VLM在像素参考和跨数据集相机参数上的歧义性。

**技术框架**：DepthLM的整体框架包括以下几个关键步骤：1) 使用预训练的VLM作为基础模型。2) 利用稀疏的深度标签，通过文本监督微调VLM。3) 引入视觉提示（Visual Prompting）来帮助VLM更好地理解像素级别的深度信息。4) 使用内在条件增强（Intrinsic-Conditioned Augmentation）来解决跨数据集的相机参数歧义问题。

**关键创新**：DepthLM最重要的技术创新在于，它证明了通过简单的文本监督微调，即可解锁VLM在度量深度估计方面的潜力，而无需复杂的架构修改或损失函数设计。此外，视觉提示和内在条件增强有效地解决了VLM在像素参考和相机参数方面的固有问题。

**关键设计**：在视觉提示方面，论文可能使用了可学习的prompt tokens，添加到输入图像的embedding中，引导VLM关注与深度相关的特征。在内在条件增强方面，可能通过对训练数据进行相机参数的归一化或数据增强，来减少跨数据集的相机参数差异。损失函数方面，可能使用了简单的L1或L2损失，直接回归预测的深度值。

## 📊 实验亮点

DepthLM在度量深度估计任务上取得了显著的性能提升，超越了现有最先进的VLM 2倍以上，并且与纯视觉模型达到了可比的精度。更重要的是，DepthLM在训练过程中没有明确强制执行的情况下，自然地避免了过度平滑问题，在边界区域的悬浮点明显少于纯视觉模型。

## 🎯 应用场景

DepthLM的潜在应用领域包括机器人导航、自动驾驶、三维重建、虚拟现实和增强现实等。该研究的实际价值在于，它提供了一种简单有效的方法，使VLM能够理解3D场景，从而促进了VLM在3D视觉任务中的应用。未来，DepthLM可以进一步扩展到其他3D任务，例如场景理解、物体识别和姿态估计等。

## 📄 摘要（原文）

> Vision language models (VLMs) can flexibly address various vision tasks through text interactions. Although successful in semantic understanding, state-of-the-art VLMs including GPT-5 still struggle in understanding 3D from 2D inputs. On the other hand, expert pure vision models achieve super-human accuracy in metric depth estimation, a key 3D understanding task. However, they require task-specific architectures and losses. Such difference motivates us to ask: Can VLMs reach expert-level accuracy without architecture or loss change? We take per-pixel metric depth estimation as the representative task and show that the answer is yes! Surprisingly, comprehensive analysis shows that text-based supervised-finetuning with sparse labels is sufficient for VLMs to unlock strong 3D understanding, no dense prediction head or complex regression/regularization loss is needed. The bottleneck for VLMs lies actually in pixel reference and cross-dataset camera ambiguity, which we address through visual prompting and intrinsic-conditioned augmentation. With much smaller models, our method DepthLM surpasses the accuracy of most advanced VLMs by over 2x, making VLMs for the first time comparable with pure vision models. Interestingly, without explicit enforcement during training, VLMs trained with DepthLM naturally avoids over-smoothing, having much fewer flying points at boundary regions than pure vision models. The simplicity of DepthLM also enables a single VLM to cover various 3D tasks beyond metric depth. Our code and model will be released at the link below.

