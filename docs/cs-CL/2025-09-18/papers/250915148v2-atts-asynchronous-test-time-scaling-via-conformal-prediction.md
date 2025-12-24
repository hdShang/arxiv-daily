---
layout: default
title: "ATTS: Asynchronous Test-Time Scaling via Conformal Prediction"
---

# ATTS: Asynchronous Test-Time Scaling via Conformal Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15148" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15148v2</a>
  <a href="https://arxiv.org/pdf/2509.15148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15148v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15148v2', 'ATTS: Asynchronous Test-Time Scaling via Conformal Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Xiong, Qiujiang Chen, Fanghua Ye, Zhongwei Wan, Chuanyang Zheng, Chenyang Zhao, Hui Shen, Alexander Hanbo Li, Chaofan Tao, Haochen Tan, Haoli Bai, Lifeng Shang, Lingpeng Kong, Ngai Wong

**分类**: cs.CL

**发布日期**: 2025-09-18 (更新: 2025-09-28)

**备注**: Tech Report

**🔗 代码/项目**: [GITHUB](https://github.com/menik1126/asynchronous-test-time-scaling)

---

## 💡 一句话要点

**提出ATTS：一种基于保形预测的异步测试时缩放框架，显著加速LLM推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `测试时缩放` `推测解码` `异步推理` `保形预测`

## 📋 核心要点

1. 现有LLM测试时缩放受限于高推理延迟和同步开销，尤其是在并行和顺序维度同时缩放时。
2. ATTS通过在线校准实现异步推理，并利用序数分类算法支持三阶段拒绝采样，从而实现高效的并行和顺序缩放。
3. 实验表明，ATTS在多个数据集上实现了显著的加速和吞吐量提升，同时保持了精度，并降低了延迟和内存开销。

## 📝 摘要（中文）

大型语言模型（LLM）受益于测试时缩放，但常常受到高推理延迟的阻碍。推测解码是加速缩放过程的一种自然方式；然而，沿并行和顺序维度进行缩放都带来了重大挑战，包括大量的内存密集型执行和同步开销。我们引入了ATTS（异步测试时缩放），这是一个统计保证的自适应缩放框架，它遵循假设检验过程来解决这些挑战。通过重新审视算术强度，ATTS将同步确定为主要瓶颈。它通过在线校准实现异步推理，并提出了一种支持三阶段拒绝采样管道的序数分类算法，从而沿顺序和并行轴进行缩放。在MATH、AMC23、AIME24和AIME25数据集以及多个draft-target模型家族的实验中，我们表明ATTS在测试时缩放中提供了高达56.7倍的加速和4.14倍的吞吐量提升，同时保持对拒绝率的精确控制，降低延迟和内存开销，并且不会造成精度损失。通过在并行和顺序维度上进行缩放，我们使1.5B/70B draft/target模型组合能够在AIME数据集上实现最先进的推理模型o3-mini (high)的性能。我们已在https://github.com/menik1126/asynchronous-test-time-scaling上发布了代码。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在测试时缩放过程中，由于高推理延迟和同步开销导致的效率瓶颈问题。现有的推测解码方法在并行和顺序维度上同时缩放时，会面临严重的内存密集型执行和同步开销，限制了整体性能的提升。

**核心思路**：ATTS的核心思路是通过异步推理来消除同步瓶颈。它基于假设检验过程，采用统计保证的自适应缩放框架，允许draft模型和target模型异步执行，从而减少等待时间，提高资源利用率。通过在线校准，ATTS能够动态调整缩放策略，以适应不同的输入和模型状态。

**技术框架**：ATTS框架包含以下主要阶段：1) **在线校准**：根据历史数据动态调整缩放参数，保证统计有效性。2) **三阶段拒绝采样**：利用序数分类算法，对draft模型的预测进行多轮验证，逐步提高预测的置信度。3) **异步推理**：draft模型和target模型异步执行，减少同步等待时间。整个流程旨在实现高效的并行和顺序缩放，同时保持精度。

**关键创新**：ATTS的关键创新在于其异步推理机制和在线校准策略。传统的推测解码方法通常需要同步等待draft模型和target模型的结果，而ATTS通过异步执行，显著减少了等待时间。在线校准则能够根据实际情况动态调整缩放参数，提高了框架的适应性和鲁棒性。

**关键设计**：ATTS的关键设计包括：1) **序数分类算法**：用于对draft模型的预测进行多轮验证，输出置信度等级。2) **在线校准策略**：基于保形预测，动态调整缩放参数，保证统计有效性。3) **三阶段拒绝采样管道**：通过多轮验证，逐步提高预测的置信度，减少错误预测的概率。具体的参数设置和损失函数选择取决于具体的模型和数据集。

## 📊 实验亮点

ATTS在MATH、AMC23、AIME24和AIME25数据集上进行了广泛的实验，结果表明，ATTS在测试时缩放中提供了高达56.7倍的加速和4.14倍的吞吐量提升，同时保持了对拒绝率的精确控制，降低了延迟和内存开销，并且没有造成精度损失。通过并行和顺序维度缩放，1.5B/70B draft/target模型组合在AIME数据集上达到了最先进的推理模型o3-mini (high)的性能。

## 🎯 应用场景

ATTS可广泛应用于需要快速推理的大型语言模型应用场景，例如在线问答、机器翻译、文本生成等。该技术能够显著降低推理延迟，提高用户体验，并降低计算成本。未来，ATTS有望进一步扩展到其他类型的模型和任务，例如图像识别、语音识别等。

## 📄 摘要（原文）

> Large language models (LLMs) benefit from test-time scaling but are often hampered by high inference latency. Speculative decoding is a natural way to accelerate the scaling process; however, scaling along both the parallel and sequential dimensions poses significant challenges, including substantial memory-bound execution and synchronization overhead. We introduce ATTS (Asynchronous Test-Time Scaling), a statistically guaranteed adaptive scaling framework that follows the hypothesis testing process to address these challenges. By revisiting arithmetic intensity, ATTS identifies synchronization as the primary bottleneck. It enables asynchronous inference through online calibration and proposes an ordinal classification algorithm that supports a three-stage rejection sampling pipeline, scaling along both the sequential and parallel axes. Across experiments on the MATH, AMC23, AIME24, and AIME25 datasets and across multiple draft-target model families, we show that ATTS delivers up to 56.7x speedup in test-time scaling and a 4.14x throughput improvement, while maintaining accurate control of the rejection rate, reducing latency and memory overhead, and incurring no accuracy loss. By scaling both in parallel and sequential dimensions, we enable the 1.5B/70B draft/target model combination to achieve the performance of the state-of-the-art reasoning model o3-mini (high) on the AIME dataset. We have released the code at https://github.com/menik1126/asynchronous-test-time-scaling.

