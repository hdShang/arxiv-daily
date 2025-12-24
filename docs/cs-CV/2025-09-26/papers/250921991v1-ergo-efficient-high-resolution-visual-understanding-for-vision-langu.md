---
layout: default
title: "ERGO: Efficient High-Resolution Visual Understanding for Vision-Language Models"
---

# ERGO: Efficient High-Resolution Visual Understanding for Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21991" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21991v1</a>
  <a href="https://arxiv.org/pdf/2509.21991.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21991v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21991v1', 'ERGO: Efficient High-Resolution Visual Understanding for Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jewon Lee, Wooksu Shin, Seungmin Yang, Ki-Ung Song, DongUk Lim, Jaeyeon Kim, Tae-Ho Kim, Bo-Kyeong Kim

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-26

**🔗 代码/项目**: [GITHUB](https://github.com/nota-github/ERGO)

---

## 💡 一句话要点

**提出ERGO，通过粗到精推理提升视觉语言模型在高分辨率图像理解中的效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `高分辨率图像` `粗到精推理` `强化学习` `推理驱动感知`

## 📋 核心要点

1. 现有视觉语言模型处理高分辨率图像时，由于视觉tokens数量庞大，导致计算开销显著增加。
2. ERGO采用两阶段粗到精推理，先识别任务相关区域，再对这些区域进行全分辨率处理，降低计算成本。
3. ERGO在V*基准测试中超越Qwen2.5-VL-7B 4.7个点，同时仅使用23%的视觉tokens，推理速度提升3倍。

## 📝 摘要（中文）

为了在实际视觉语言应用中高效处理高分辨率图像，本文提出了一种名为ERGO（Efficient Reasoning & Guided Observation）的两阶段“粗到精”推理流程。该流程首先分析降采样图像以识别任务相关的区域，然后仅裁剪这些区域并以全分辨率进行后续推理。这种方法在降低计算成本的同时，保留了必要的精细视觉细节。ERGO通过利用多模态上下文执行推理驱动的感知，从而确定关注区域，解决了现有方法在输入图像降采样后第一阶段的失效问题。该模型可以考虑感知不确定性，扩大裁剪区域以覆盖视觉模糊区域，从而更准确地回答问题。通过在强化学习框架中开发简单而有效的奖励组件，实现了粗到精的感知。在多个数据集上的实验表明，ERGO在效率更高的情况下，比原始模型和竞争方法具有更高的准确性。例如，ERGO在V*基准测试中超过Qwen2.5-VL-7B 4.7个点，同时仅使用23%的视觉tokens，实现了3倍的推理加速。

## 🔬 方法详解

**问题定义**：现有的大型视觉语言模型（LVLMs）在处理高分辨率图像时面临巨大的计算负担，因为视觉tokens的数量非常庞大。尤其是在“用图像思考”的模型中，推理不仅限于文本，还扩展到视觉领域，这使得高效处理高分辨率图像变得更加重要。现有的方法，特别是那些依赖于感知驱动推理的方法，在图像降采样后往往会失效，因为它们需要清晰的视觉信息才能进行有效的推理。

**核心思路**：ERGO的核心思路是采用一种两阶段的“粗到精”推理流程。首先，对降采样后的图像进行分析，以识别与给定查询相关的区域。然后，仅将这些区域裁剪出来，并以全分辨率进行处理，用于后续的推理阶段。这种方法旨在减少计算成本，同时保留必要的精细视觉细节。ERGO通过推理驱动的感知，利用多模态上下文来确定应该关注哪些区域，从而克服了现有方法在降采样图像上的失效问题。

**技术框架**：ERGO的整体框架包含两个主要阶段：粗略感知阶段和精细推理阶段。在粗略感知阶段，模型接收降采样后的图像和文本查询作为输入，并使用强化学习来学习如何选择与查询相关的区域。在精细推理阶段，模型将裁剪出的高分辨率区域与原始文本查询结合起来，进行最终的推理和答案生成。强化学习框架用于优化区域选择策略，奖励模型选择能够产生准确答案的区域。

**关键创新**：ERGO的关键创新在于其推理驱动的感知机制。与传统的感知驱动推理不同，ERGO利用多模态上下文（包括文本查询）来指导视觉区域的选择。这种方法允许模型在感知不确定性存在的情况下，扩大裁剪区域以覆盖视觉模糊的区域，从而提高答案的准确性。此外，ERGO使用强化学习来优化区域选择策略，使其能够自适应地学习如何选择最相关的区域。

**关键设计**：ERGO的强化学习框架包含多个奖励组件，旨在鼓励模型选择能够产生准确答案的区域。这些奖励组件包括：准确性奖励，用于奖励模型生成正确答案；效率奖励，用于惩罚模型选择过大的区域；以及覆盖率奖励，用于鼓励模型覆盖视觉模糊的区域。模型使用Actor-Critic算法进行训练，Actor网络负责选择区域，Critic网络负责评估所选区域的质量。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

ERGO在多个数据集上取得了显著的性能提升。在V*基准测试中，ERGO超越了Qwen2.5-VL-7B 4.7个点，同时仅使用了23%的视觉tokens，实现了3倍的推理加速。实验结果表明，ERGO能够在保持甚至提高准确性的同时，显著降低计算成本，使其成为高分辨率视觉语言任务的有效解决方案。代码和模型已开源。

## 🎯 应用场景

ERGO适用于需要处理高分辨率图像的各种视觉语言任务，例如视觉问答、图像描述、目标检测等。该方法可以应用于自动驾驶、医疗影像分析、智能零售等领域，提高模型在资源受限环境下的性能和效率。未来，ERGO可以进一步扩展到处理视频等多模态数据，并与其他高效推理技术相结合，实现更强大的视觉语言理解能力。

## 📄 摘要（原文）

> Efficient processing of high-resolution images is crucial for real-world vision-language applications. However, existing Large Vision-Language Models (LVLMs) incur substantial computational overhead due to the large number of vision tokens. With the advent of "thinking with images" models, reasoning now extends beyond text to the visual domain. This capability motivates our two-stage "coarse-to-fine" reasoning pipeline: first, a downsampled image is analyzed to identify task-relevant regions; then, only these regions are cropped at full resolution and processed in a subsequent reasoning stage. This approach reduces computational cost while preserving fine-grained visual details where necessary. A major challenge lies in inferring which regions are truly relevant to a given query. Recent related methods often fail in the first stage after input-image downsampling, due to perception-driven reasoning, where clear visual information is required for effective reasoning. To address this issue, we propose ERGO (Efficient Reasoning & Guided Observation) that performs reasoning-driven perception-leveraging multimodal context to determine where to focus. Our model can account for perceptual uncertainty, expanding the cropped region to cover visually ambiguous areas for answering questions. To this end, we develop simple yet effective reward components in a reinforcement learning framework for coarse-to-fine perception. Across multiple datasets, our approach delivers higher accuracy than the original model and competitive methods, with greater efficiency. For instance, ERGO surpasses Qwen2.5-VL-7B on the V* benchmark by 4.7 points while using only 23% of the vision tokens, achieving a 3x inference speedup. The code and models can be found at: https://github.com/nota-github/ERGO.

