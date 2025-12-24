---
layout: default
title: "LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning"
---

# LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18841" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18841v1</a>
  <a href="https://arxiv.org/pdf/2506.18841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18841v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18841v1', 'LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhao Wu, Yushi Bai, Zhiqiang Hu, Roy Ka-Wei Lee, Juanzi Li

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-23

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/THU-KEG/LongWriter-Zero-32B)

---

## 💡 一句话要点

**提出LongWriter-Zero以解决超长文本生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超长文本生成` `强化学习` `大型语言模型` `自然语言处理` `文本质量优化`

## 📋 核心要点

1. 现有方法如LongWriter依赖合成数据进行监督微调，导致生成文本缺乏一致性和自然性。
2. 本文提出了一种基于强化学习的激励方法，从零开始训练LLMs，无需合成或标注数据。
3. LongWriter-Zero在长文本写作任务中表现优异，超越传统方法和大型模型，达到了最新的性能指标。

## 📝 摘要（中文）

超长文本生成是大型语言模型（LLMs）面临的重要挑战，现有方法如LongWriter依赖于合成数据进行监督微调，存在数据构建困难、缺乏一致性和自然性等问题。本文提出了一种基于激励的强化学习方法，从零开始训练LLMs，旨在提升超长文本生成的质量和控制能力。实验结果表明，LongWriter-Zero在长文本写作任务中显著优于传统的监督微调方法，达到了WritingBench和Arena-Write上的最新成果，甚至超越了100B+模型。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在超长文本生成中的质量下降和生成长度限制问题。现有方法依赖于合成数据，导致生成文本的自然性和一致性不足。

**核心思路**：提出了一种基于强化学习的激励机制，从零开始训练模型，旨在通过奖励机制引导模型生成高质量的超长文本。

**技术框架**：整体架构包括基于强化学习的训练流程，使用专门的奖励模型来引导生成过程，确保文本长度控制、写作质量和结构格式的优化。

**关键创新**：最重要的创新点在于完全不依赖合成或标注数据，通过强化学习实现超长文本生成能力的自我提升，这与传统的监督微调方法本质上不同。

**关键设计**：在训练过程中，采用了特定的奖励模型来评估生成文本的质量，并设计了适当的损失函数以优化模型的生成策略。

## 📊 实验亮点

实验结果显示，LongWriter-Zero在WritingBench和Arena-Write的长文本写作任务中，超越了传统的监督微调方法，达到了最新的性能指标，且在与100B+模型如DeepSeek R1和Qwen3-235B的对比中表现优异，显示出显著的提升幅度。

## 🎯 应用场景

该研究的潜在应用领域包括内容创作、自动化写作、长篇报告生成等，能够为教育、媒体和商业等行业提供高效的文本生成解决方案。未来，该技术可能推动更自然和连贯的长文本生成，提升人机交互的质量。

## 📄 摘要（原文）

> Ultra-long generation by large language models (LLMs) is a widely demanded scenario, yet it remains a significant challenge due to their maximum generation length limit and overall quality degradation as sequence length increases. Previous approaches, exemplified by LongWriter, typically rely on ''teaching'', which involves supervised fine-tuning (SFT) on synthetic long-form outputs. However, this strategy heavily depends on synthetic SFT data, which is difficult and costly to construct, often lacks coherence and consistency, and tends to be overly artificial and structurally monotonous. In this work, we propose an incentivization-based approach that, starting entirely from scratch and without relying on any annotated or synthetic data, leverages reinforcement learning (RL) to foster the emergence of ultra-long, high-quality text generation capabilities in LLMs. We perform RL training starting from a base model, similar to R1-Zero, guiding it to engage in reasoning that facilitates planning and refinement during the writing process. To support this, we employ specialized reward models that steer the LLM towards improved length control, writing quality, and structural formatting. Experimental evaluations show that our LongWriter-Zero model, trained from Qwen2.5-32B, consistently outperforms traditional SFT methods on long-form writing tasks, achieving state-of-the-art results across all metrics on WritingBench and Arena-Write, and even surpassing 100B+ models such as DeepSeek R1 and Qwen3-235B. We open-source our data and model checkpoints under https://huggingface.co/THU-KEG/LongWriter-Zero-32B

