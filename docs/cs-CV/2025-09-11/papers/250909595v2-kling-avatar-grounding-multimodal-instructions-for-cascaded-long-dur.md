---
layout: default
title: "Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis"
---

# Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09595" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09595v2</a>
  <a href="https://arxiv.org/pdf/2509.09595.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09595v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09595v2', 'Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yikang Ding, Jiwen Liu, Wenyuan Zhang, Zekun Wang, Wentao Hu, Liyuan Cui, Mingming Lao, Yingchao Shao, Hui Liu, Xiaohan Li, Ming Chen, Xiaoqiang Liu, Yu-Shen Liu, Pengfei Wan

**分类**: cs.CV

**发布日期**: 2025-09-11 (更新: 2025-09-17)

**备注**: Technical Report. Project Page: https://klingavatar.github.io/

---

## 💡 一句话要点

**Kling-Avatar：通过多模态指令驱动的级联式长时程虚拟形象动画合成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚拟形象生成` `多模态指令` `长时程视频` `大语言模型` `级联框架`

## 📋 核心要点

1. 现有音频驱动虚拟形象生成方法缺乏对指令中交流目的的建模，导致叙事性和角色表现力不足。
2. Kling-Avatar提出一种级联框架，利用多模态大语言模型生成蓝图视频，指导后续高保真虚拟形象生成。
3. 实验表明，Kling-Avatar在唇音同步、情感表达、指令控制等方面表现优异，并能生成高分辨率长时程视频。

## 📝 摘要（中文）

本文提出Kling-Avatar，一种新颖的级联框架，旨在统一多模态指令理解与照片级真实感的虚拟形象生成。现有音频驱动的虚拟形象视频生成方法仅将指令条件反射视为由声音或视觉线索驱动的低级跟踪，忽略了指令所传达的交流目的，从而影响了叙事连贯性和角色表现力。Kling-Avatar采用两阶段流程：首先，设计一个多模态大型语言模型（MLLM）导演，根据不同的指令信号生成蓝图视频，从而控制角色运动和情绪等高级语义。其次，在蓝图关键帧的指导下，使用首尾帧策略并行生成多个子片段。这种全局到局部的框架保留了精细的细节，同时忠实地编码了多模态指令背后的高级意图。并行架构还能够快速稳定地生成长时程视频，适用于数字人直播和视频博客等实际应用。构建了一个包含375个精选样本的基准，涵盖了不同的指令和具有挑战性的场景，以全面评估该方法。实验结果表明，Kling-Avatar能够生成生动、流畅、长时程的视频，分辨率高达1080p，帧率高达48fps，在唇音同步准确性、情感和动态表现力、指令可控性、身份保持和跨域泛化方面均表现出卓越的性能。Kling-Avatar为语义驱动的高保真音频驱动虚拟形象合成建立了一个新的基准。

## 🔬 方法详解

**问题定义**：现有音频驱动的虚拟形象生成方法主要关注于音频和视觉线索的低级跟踪，忽略了指令中的高级语义信息和交流目的。这导致生成的虚拟形象在叙事连贯性和角色情感表达方面存在不足，难以满足数字人直播、视频博客等实际应用的需求。

**核心思路**：Kling-Avatar的核心思路是将多模态指令理解与虚拟形象生成解耦，通过一个多模态大语言模型（MLLM）作为“导演”，理解指令并生成包含高级语义信息的蓝图视频。然后，利用蓝图视频指导后续的高保真虚拟形象生成，从而实现对指令的精确控制和更丰富的角色表达。

**技术框架**：Kling-Avatar采用两阶段级联框架：
1. **MLLM导演阶段**：利用多模态大语言模型（MLLM）接收文本、音频等多种指令信号，生成包含角色运动、情感等高级语义信息的蓝图视频。
2. **虚拟形象生成阶段**：根据蓝图视频的关键帧，并行生成多个子片段。该阶段采用首尾帧策略，保证视频的连贯性和流畅性。

**关键创新**：Kling-Avatar的关键创新在于引入了多模态大语言模型（MLLM）作为“导演”，将指令理解与虚拟形象生成分离。这种设计使得模型能够更好地理解指令中的高级语义信息，并将其转化为具体的角色行为和情感表达。此外，并行生成子片段的策略提高了生成效率，使得模型能够生成长时程的视频。

**关键设计**：
* **MLLM导演**：具体采用的MLLM架构以及训练数据未明确说明，但强调了其对多模态指令的理解能力。
* **蓝图视频**：蓝图视频的具体表示形式（例如，关键点、姿态等）未知。
* **首尾帧策略**：通过约束子片段的首尾帧，保证视频的连贯性。
* **损失函数**：具体的损失函数设计未知，但强调了对唇音同步、情感表达等方面的优化。

## 📊 实验亮点

Kling-Avatar在多个指标上取得了显著的性能提升。在唇音同步准确性、情感和动态表现力、指令可控性、身份保持和跨域泛化方面均优于现有方法。该模型能够生成高达1080p分辨率和48fps帧率的流畅长时程视频，并在包含375个样本的基准测试中表现出色，证明了其在复杂场景下的有效性和鲁棒性。

## 🎯 应用场景

Kling-Avatar具有广泛的应用前景，包括数字人直播、虚拟视频博客、虚拟助手、在线教育等领域。该技术能够生成逼真、可控的虚拟形象，为用户提供更具沉浸感和互动性的体验。未来，该技术有望应用于游戏、社交媒体等更多领域，推动人机交互方式的变革。

## 📄 摘要（原文）

> Recent advances in audio-driven avatar video generation have significantly enhanced audio-visual realism. However, existing methods treat instruction conditioning merely as low-level tracking driven by acoustic or visual cues, without modeling the communicative purpose conveyed by the instructions. This limitation compromises their narrative coherence and character expressiveness. To bridge this gap, we introduce Kling-Avatar, a novel cascaded framework that unifies multimodal instruction understanding with photorealistic portrait generation. Our approach adopts a two-stage pipeline. In the first stage, we design a multimodal large language model (MLLM) director that produces a blueprint video conditioned on diverse instruction signals, thereby governing high-level semantics such as character motion and emotions. In the second stage, guided by blueprint keyframes, we generate multiple sub-clips in parallel using a first-last frame strategy. This global-to-local framework preserves fine-grained details while faithfully encoding the high-level intent behind multimodal instructions. Our parallel architecture also enables fast and stable generation of long-duration videos, making it suitable for real-world applications such as digital human livestreaming and vlogging. To comprehensively evaluate our method, we construct a benchmark of 375 curated samples covering diverse instructions and challenging scenarios. Extensive experiments demonstrate that Kling-Avatar is capable of generating vivid, fluent, long-duration videos at up to 1080p and 48 fps, achieving superior performance in lip synchronization accuracy, emotion and dynamic expressiveness, instruction controllability, identity preservation, and cross-domain generalization. These results establish Kling-Avatar as a new benchmark for semantically grounded, high-fidelity audio-driven avatar synthesis.

