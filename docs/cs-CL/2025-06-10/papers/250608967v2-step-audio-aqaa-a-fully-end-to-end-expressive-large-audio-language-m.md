---
layout: default
title: "Step-Audio-AQAA: a Fully End-to-End Expressive Large Audio Language Model"
---

# Step-Audio-AQAA: a Fully End-to-End Expressive Large Audio Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08967" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08967v2</a>
  <a href="https://arxiv.org/pdf/2506.08967.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08967v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08967v2', 'Step-Audio-AQAA: a Fully End-to-End Expressive Large Audio Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ailin Huang, Bingxin Li, Bruce Wang, Boyong Wu, Chao Yan, Chengli Feng, Heng Wang, Hongyu Zhou, Hongyuan Wang, Jingbei Li, Jianjian Sun, Joanna Wang, Mingrui Chen, Peng Liu, Ruihang Miao, Shilei Jiang, Tian Fei, Wang You, Xi Chen, Xuerui Yang, Yechang Huang, Yuxiang Zhang, Zheng Ge, Zheng Gong, Zhewei Huang, Zixin Zhang, Bin Wang, Bo Li, Buyun Ma, Changxin Miao, Changyi Wan, Chen Xu, Dapeng Shi, Dingyuan Hu, Enle Liu, Guanzhe Huang, Gulin Yan, Hanpeng Hu, Haonan Jia, Jiahao Gong, Jiaoren Wu, Jie Wu, Jie Yang, Junzhe Lin, Kaixiang Li, Lei Xia, Longlong Gu, Ming Li, Nie Hao, Ranchen Ming, Shaoliang Pang, Siqi Liu, Song Yuan, Tiancheng Cao, Wen Li, Wenqing He, Xu Zhao, Xuelin Zhang, Yanbo Yu, Yinmin Zhong, Yu Zhou, Yuanwei Liang, Yuanwei Lu, Yuxiang Yang, Zidong Yang, Zili Zhang, Binxing Jiao, Heung-Yeung Shum, Jiansheng Chen, Jing Li, Xiangyu Zhang, Xinhao Zhang, Yibo Zhu, Daxin Jiang, Shuchang Zhou, Chen Hu

**分类**: cs.SD, cs.CL, eess.AS

**发布日期**: 2025-06-10 (更新: 2025-06-13)

**备注**: 12 pages, 3 figures

---

## 💡 一句话要点

**提出Step-Audio-AQAA以解决音频交互中的自然语言生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `音频语言模型` `自然语言生成` `音频交互` `神经声码器` `语音合成` `直接偏好优化` `全端到端模型`

## 📋 核心要点

1. 现有大型音频语言模型在生成自然语音响应方面存在局限，影响了音频交互的流畅性。
2. Step-Audio-AQAA通过集成双代码本音频标记器和1300亿参数的LLM，提供全端到端的音频查询-音频回答解决方案。
3. 在StepEval-Audio-360基准测试中，Step-Audio-AQAA在语音控制等关键领域表现优于现有最先进模型。

## 📝 摘要（中文）

大型音频语言模型（LALMs）在智能人机交互中取得了显著进展，但其依赖文本输出的特性限制了自然语音响应的生成，妨碍了无缝音频交互。为此，我们提出了Step-Audio-AQAA，这是一种针对音频查询-音频回答（AQAA）任务的全端到端LALM。该模型集成了双代码本音频标记器用于语言和语义特征提取，采用1300亿参数的主干LLM和神经声码器进行高保真语音合成。我们的后训练方法通过交错的文本和音频输出增强语义一致性，并结合直接偏好优化（DPO）与模型合并以提升性能。在StepEval-Audio-360基准上的评估表明，Step-Audio-AQAA在语音控制方面表现优异，超越了当前最先进的LALMs。此项工作为全端到端LALMs提供了有前景的解决方案，并强调了基于标记的声码器在提升AQAA任务整体性能中的关键作用。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大型音频语言模型在生成自然语音响应时的局限性，尤其是在音频交互场景中，文本输出的依赖性导致了交互的生硬与不自然。

**核心思路**：论文提出的Step-Audio-AQAA模型通过全端到端的设计，结合音频查询与音频回答的任务，旨在实现更自然的音频交互体验。通过双代码本音频标记器提取语言和语义特征，增强了模型的表达能力。

**技术框架**：该模型的整体架构包括三个主要模块：双代码本音频标记器用于特征提取，1300亿参数的主干LLM用于理解和生成内容，以及神经声码器用于高保真语音合成。模型采用后训练方法，通过交错的文本和音频输出提升语义一致性。

**关键创新**：最重要的技术创新在于结合了直接偏好优化（DPO）与模型合并的策略，显著提升了模型在AQAA任务中的表现。这一方法与传统的单一文本输出模型形成了本质区别。

**关键设计**：在模型设计中，采用了双代码本音频标记器以实现高效的特征提取，并通过精心设计的损失函数和网络结构，确保了音频合成的高保真度和语义一致性。

## 📊 实验亮点

在StepEval-Audio-360基准测试中，Step-Audio-AQAA在语音控制任务上表现优异，超越了现有最先进的LALMs，显示出在语义一致性和自然语音生成方面的显著提升，具体性能数据尚未披露。

## 🎯 应用场景

Step-Audio-AQAA的研究成果具有广泛的应用潜力，尤其在智能助手、语音交互系统和教育领域等场景中，可以实现更自然流畅的音频交互体验。未来，该模型的技术可以推动人机交互的进一步发展，使得机器能够更好地理解和响应人类的语音指令。

## 📄 摘要（原文）

> Large Audio-Language Models (LALMs) have significantly advanced intelligent human-computer interaction, yet their reliance on text-based outputs limits their ability to generate natural speech responses directly, hindering seamless audio interactions. To address this, we introduce Step-Audio-AQAA, a fully end-to-end LALM designed for Audio Query-Audio Answer (AQAA) tasks. The model integrates a dual-codebook audio tokenizer for linguistic and semantic feature extraction, a 130-billion-parameter backbone LLM and a neural vocoder for high-fidelity speech synthesis. Our post-training approach employs interleaved token-output of text and audio to enhance semantic coherence and combines Direct Preference Optimization (DPO) with model merge to improve performance. Evaluations on the StepEval-Audio-360 benchmark demonstrate that Step-Audio-AQAA excels especially in speech control, outperforming the state-of-art LALMs in key areas. This work contributes a promising solution for end-to-end LALMs and highlights the critical role of token-based vocoder in enhancing overall performance for AQAA tasks.

