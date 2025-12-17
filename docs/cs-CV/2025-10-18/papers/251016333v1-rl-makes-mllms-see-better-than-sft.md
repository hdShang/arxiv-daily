---
layout: default
title: RL makes MLLMs see better than SFT
---

# RL makes MLLMs see better than SFT

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.16333" target="_blank" class="toolbar-btn">arXiv: 2510.16333v1</a>
    <a href="https://arxiv.org/pdf/2510.16333.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16333v1" 
            onclick="toggleFavorite(this, '2510.16333v1', 'RL makes MLLMs see better than SFT')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Junha Song, Sangdoo Yun, Dongyoon Han, Jaegul Choo, Byeongho Heo

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-18

**🔗 代码/项目**: [PROJECT_PAGE](https://june-page.github.io/pivot/)

---

## 💡 一句话要点

**提出PIVOT，利用强化学习优化MLLM视觉编码器，显著提升视觉感知能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉编码器` `强化学习` `视觉问答` `表征学习`

## 📋 核心要点

1. 现有MLLM研究过度依赖LLM，忽视了视觉编码器对模型性能的关键影响，尤其是在训练策略从SFT转向RL后。
2. 论文提出Preference-Instructed Vision OpTimization (PIVOT)方法，利用强化学习指导视觉编码器的优化，提升视觉表征能力。
3. 实验表明，PIVOT训练的视觉编码器在MLLM中表现优异，甚至超越了更大规模且训练更充分的同类模型，同时显著降低了计算成本。

## 📝 摘要（中文）

多模态语言模型(MLLM)研究中的一个主要假设是，其性能很大程度上继承自LLM骨干网络，因为LLM具有巨大的参数规模和卓越的能力。这导致了对视觉编码器的理解存在空白，而视觉编码器决定了MLLM如何感知图像。最近MLLM训练范式的转变，从监督微调(SFT)到强化学习(RL)，放大了这种疏忽——即，严重缺乏对这种训练如何重塑视觉编码器以及MLLM的分析。为了解决这个问题，我们首先研究了训练策略对MLLM的影响，其中RL在强视觉相关的VQA基准测试中显示出明显优于SFT的优势。受此启发，我们通过从ImageNet分类和分割到梯度可视化的各种深入实验，对MLLM的视觉编码器进行了关键但未被充分探索的分析。我们的结果表明，MLLM的后训练策略(即SFT或RL)不仅导致MLLM下游任务的不同结果，而且从根本上重塑了MLLM的底层视觉表示。具体来说，我们研究的关键发现是，与SFT相比，RL产生更强和更精确定位的视觉表示，从而提高了MLLM视觉编码器的能力。然后，我们将我们的发现重新构建为一个简单的配方，用于构建MLLM的强大视觉编码器，即偏好指导的视觉优化(PIVOT)。当集成到MLLM中时，经过PIVOT训练的视觉编码器甚至优于更大和训练更重的同类产品，尽管所需的计算成本不到标准视觉预训练的1%。这一结果为推进MLLM的视觉骨干网络开辟了一条有效而高效的道路。

## 🔬 方法详解

**问题定义**：现有MLLM研究主要关注LLM部分的优化，忽略了视觉编码器在多模态理解中的重要作用。特别是，当训练范式从监督微调(SFT)转向强化学习(RL)时，视觉编码器的行为变化缺乏深入分析。现有方法在视觉表征学习方面存在不足，导致MLLM在视觉相关任务中表现受限。

**核心思路**：论文的核心思路是利用强化学习(RL)来优化MLLM的视觉编码器，使其能够学习到更强和更精确定位的视觉表征。通过RL，模型可以根据偏好信号调整视觉编码器的参数，从而更好地适应下游任务的需求。这种方法旨在弥补SFT在视觉表征学习方面的不足，提升MLLM的整体性能。

**技术框架**：PIVOT (Preference-Instructed Vision OpTimization) 的整体框架包含以下几个主要模块：1) 视觉编码器：负责将输入图像转换为视觉特征表示。2) LLM：作为MLLM的语言处理核心，接收视觉特征并生成文本输出。3) 奖励模型：根据模型生成的文本输出与期望输出之间的匹配程度，提供奖励信号。4) 强化学习算法：利用奖励信号优化视觉编码器的参数。训练流程是：首先，视觉编码器将图像编码为视觉特征，然后LLM基于这些特征生成文本。奖励模型评估生成的文本，并提供奖励信号。最后，强化学习算法利用这些奖励信号更新视觉编码器的参数。

**关键创新**：最重要的技术创新点在于使用强化学习来直接优化视觉编码器，而不是像传统方法那样依赖于监督学习或预训练。这种方法允许视觉编码器根据下游任务的偏好进行自适应调整，从而学习到更有效的视觉表征。与现有方法的本质区别在于，PIVOT 是一种端到端的优化方法，可以直接优化视觉编码器以适应MLLM的需求。

**关键设计**：PIVOT的关键设计包括：1) 奖励函数的设计：奖励函数需要能够准确地反映模型生成的文本输出与期望输出之间的匹配程度。可以使用诸如BLEU、ROUGE等指标来衡量文本相似度。2) 强化学习算法的选择：可以使用诸如PPO、SAC等先进的强化学习算法来优化视觉编码器的参数。3) 视觉编码器的结构：可以使用诸如ViT、ResNet等常用的视觉编码器结构。4) 偏好数据的构建：需要构建包含偏好信息的训练数据，例如，对于VQA任务，可以提供多个可能的答案，并根据其正确性进行排序。

## 📊 实验亮点

实验结果表明，使用PIVOT训练的视觉编码器在多个VQA基准测试中表现优异，超越了使用SFT训练的同类模型。更重要的是，PIVOT训练的视觉编码器甚至优于更大规模且训练更充分的同类模型，同时显著降低了计算成本，计算成本低于标准视觉预训练的1%。

## 🎯 应用场景

该研究成果可广泛应用于多模态理解领域，例如视觉问答、图像描述、视觉推理等。通过提升MLLM的视觉感知能力，可以改善人机交互体验，提高自动化系统的智能化水平。未来，该方法有望应用于智能客服、自动驾驶、医疗诊断等领域。

## 📄 摘要（原文）

> A dominant assumption in Multimodal Language Model (MLLM) research is that its performance is largely inherited from the LLM backbone, given its immense parameter scale and remarkable capabilities. This has created a void in the understanding of the vision encoder, which determines how MLLMs perceive images. The recent shift in MLLM training paradigms, from Supervised Finetuning (SFT) to Reinforcement Learning (RL), magnifies this oversight-namely, the significant lack of analysis on how such training reshapes the vision encoder as well as the MLLM. To address this, we first investigate the impact of training strategies on MLLMs, where RL shows a clear advantage over SFT in strongly vision-related VQA benchmarks. Motivated by this, we conduct a critical yet under-explored analysis of the vision encoder of MLLMs through diverse and in-depth experiments, ranging from ImageNet classification and segmentation to gradient visualization. Our results demonstrate that MLLM's post-training strategy (i.e., SFT or RL) not only leads to distinct outcomes on MLLM downstream tasks, but also fundamentally reshapes MLLM's underlying visual representations. Specifically, the key finding of our study is that RL produces stronger and precisely localized visual representations compared to SFT, boosting the ability of the vision encoder for MLLM. We then reframe our findings into a simple recipe for building strong vision encoders for MLLMs, Preference-Instructed Vision OpTimization (PIVOT). When integrated into MLLMs, a PIVOT-trained vision encoder outperforms even larger and more heavily-trained counterparts, despite requiring less than 1% of the computational cost of standard vision pretraining. This result opens an effective and efficient path for advancing the vision backbones of MLLMs. Project page available at https://june-page.github.io/pivot/

