---
layout: default
title: DeepDiver: Adaptive Search Intensity Scaling via Open-Web Reinforcement Learning
---

# DeepDiver: Adaptive Search Intensity Scaling via Open-Web Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24332" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24332v2</a>
  <a href="https://arxiv.org/pdf/2505.24332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24332v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24332v2', 'DeepDiver: Adaptive Search Intensity Scaling via Open-Web Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxuan Shi, Haochen Tan, Chuqiao Kuang, Xiaoguang Li, Xiaozhe Ren, Chen Zhang, Hanting Chen, Yasheng Wang, Lu Hou, Lifeng Shang

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-11-10)

**备注**: Accepted as NeurIPS 2025 Spotlight

---

## 💡 一句话要点

**提出DeepDiver以解决开放网络问答中的信息获取问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息获取` `强化学习` `大型语言模型` `开放网络问答` `自适应搜索` `WebPuzzle` `搜索强度扩展`

## 📋 核心要点

1. 现有方法在开放网络问答中面临信息获取的挑战，尤其是在证据收集和推理方面的不足。
2. 提出DeepDiver框架，通过强化学习培养搜索强度扩展能力，提升信息获取的频率和深度。
3. 实验结果显示，DeepDiver使得Qwen2.5-7B-Instruct和Pangu-7B-Reasoner在真实网络任务中表现优越，接近更大模型的性能。

## 📝 摘要（中文）

信息获取需要迭代的证据收集和反思推理，但现有的大型语言模型（LLMs）在开放网络问答中仍面临挑战。现有的提示和监督微调方法受到提示规则或训练语料的限制，通常仅在结构良好的维基来源上进行基准测试，限制了其在现实世界中的适应性。我们引入了WebPuzzle，一个包含24,000个样本的训练和275个样本的测试基准，评估在实时互联网环境下的信息获取。基于7,000个WebPuzzle实例，我们开发了DeepDiver，一个强化学习框架，培养搜索强度扩展（SIS）能力，使模型能够提高搜索频率和深度，而不是停留在过于自信且证据不足的答案上。通过SIS，Qwen2.5-7B-Instruct和Pangu-7B-Reasoner在真实网络任务中的表现可与671B参数的DeepSeek-R1相媲美。我们的结果推动了LLMs中自适应信息获取的发展，并为未来的研究提供了严格的基准。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在开放网络问答中信息获取的不足，现有方法往往依赖固定的提示规则或训练语料，导致适应性差。

**核心思路**：提出DeepDiver框架，通过强化学习培养搜索强度扩展（SIS）能力，使模型能够在信息获取过程中动态调整搜索频率和深度，从而提高答案的可靠性。

**技术框架**：DeepDiver的整体架构包括从冷启动的监督微调到精心设计的强化学习过程，涵盖了信息获取策略的训练与优化。

**关键创新**：DeepDiver的主要创新在于引入了搜索强度扩展（SIS）能力，使模型能够在面对开放性问题时，灵活调整其搜索策略，与传统方法相比，显著提升了信息获取的质量和深度。

**关键设计**：在模型训练中，采用了特定的损失函数和参数设置，以优化搜索策略的表现，确保模型能够有效地从开放网络中提取信息。具体的网络结构和参数细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，DeepDiver使得Qwen2.5-7B-Instruct和Pangu-7B-Reasoner在真实网络任务中的表现接近671B参数的DeepSeek-R1，展示了显著的性能提升，验证了SIS能力的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和知识管理等。通过提升大型语言模型在开放网络环境中的信息获取能力，DeepDiver能够为用户提供更为准确和可靠的答案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Information seeking demands iterative evidence gathering and reflective reasoning, yet large language models (LLMs) still struggle with it in open-web question answering. Existing prompting and supervised fine-tuning (SFT) methods remain fixed by prompt rules or training corpora, and are usually benchmarked only on well-structured wiki sources, limiting real-world adaptability. We introduce WebPuzzle, a 24k-sample training and 275-sample test benchmark that evaluates information seeking on the live internet, across both wiki and open-domain queries. Leveraging 7k WebPuzzle instances, we develop DeepDiver, a reinforcement-learning (RL) framework that cultivates Search Intensity Scaling (SIS)-an emergent ability to escalate search frequency and depth instead of settling on overconfident, under-evidenced answers. With SIS, Qwen2.5-7B-Instruct and Pangu-7B-Reasoner attain performance on real-web tasks comparable to the 671B-parameter DeepSeek-R1. We detail DeepDiver's curriculum from cold-start SFT to a well designed RL procedure, and show that its seeking policy generalized from closed-ended queries to open-ended generation such as long-form writing. Our results advance adaptive information seeking in LLMs and provide a rigorous benchmark for future work.

