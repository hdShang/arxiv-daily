---
layout: default
title: "VideoEval-Pro: Robust and Realistic Long Video Understanding Evaluation"
---

# VideoEval-Pro: Robust and Realistic Long Video Understanding Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14640" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14640v1</a>
  <a href="https://arxiv.org/pdf/2505.14640.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14640v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14640v1', 'VideoEval-Pro: Robust and Realistic Long Video Understanding Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Ma, Weiming Ren, Yiming Jia, Zhuofeng Li, Ping Nie, Ge Zhang, Wenhu Chen

**分类**: cs.CV

**发布日期**: 2025-05-20

**备注**: Dataset: https://huggingface.co/datasets/TIGER-Lab/VideoEval-Pro, Project Webpage: https://tiger-ai-lab.github.io/VideoEval-Pro

---

## 💡 一句话要点

**提出VideoEval-Pro以解决长视频理解评估的有效性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `多模态模型` `评估基准` `开放式问题` `视频分析`

## 📋 核心要点

1. 现有长视频理解评估基准依赖多项选择题，导致评估结果可能被猜测影响，缺乏有效性。
2. 本文提出VideoEval-Pro基准，采用开放式短答案问题，要求模型真正理解视频内容。
3. 实验结果显示，视频LMMs在开放式问题上的表现较MCQs显著下降，且增加输入帧数对评估效果有积极影响。

## 📝 摘要（中文）

大型多模态模型（LMMs）在长视频理解（LVU）中展现出强大能力，但现有评估基准存在显著缺陷。首先，许多基准依赖多项选择题（MCQs），其结果可能因猜测而被夸大；其次，部分问题具有强先验，使得模型无需观看视频即可回答。为此，本文提出VideoEval-Pro，一个包含开放式短答案的问题基准，真正要求理解整个视频。通过评估21个视频LMMs，发现开放式问题的表现较MCQs下降超过25%，且MCQs得分高并不意味着开放式得分高。VideoEval-Pro提供了更可靠的长视频理解评估。

## 🔬 方法详解

**问题定义**：本文旨在解决现有长视频理解评估基准的有效性问题，现有方法因依赖多项选择题而导致评估结果不可靠。

**核心思路**：提出VideoEval-Pro基准，采用开放式短答案问题，要求模型全面理解视频内容，避免简单猜测。

**技术框架**：VideoEval-Pro评估包括段落级和全视频理解，结合感知和推理任务，确保模型对视频的全面理解。

**关键创新**：最重要的创新在于引入开放式问题，显著提高了评估的真实性和可靠性，与传统的多项选择题评估方法形成鲜明对比。

**关键设计**：在设计中，问题设置强调对视频内容的深度理解，评估框架涵盖多种任务类型，确保模型在不同场景下的表现均得到考量。

## 📊 实验亮点

实验结果显示，视频LMMs在开放式问题上的表现较多项选择题下降超过25%。此外，VideoEval-Pro的设计使得增加输入帧数对评估效果的提升更为显著，提供了更真实的长视频理解评估标准。

## 🎯 应用场景

该研究的潜在应用领域包括视频内容分析、智能监控、教育视频评估等。通过提供更可靠的评估基准，VideoEval-Pro能够帮助研究者和开发者更好地理解和改进长视频理解模型，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Large multimodal models (LMMs) have recently emerged as a powerful tool for long video understanding (LVU), prompting the development of standardized LVU benchmarks to evaluate their performance. However, our investigation reveals a rather sober lesson for existing LVU benchmarks. First, most existing benchmarks rely heavily on multiple-choice questions (MCQs), whose evaluation results are inflated due to the possibility of guessing the correct answer; Second, a significant portion of questions in these benchmarks have strong priors to allow models to answer directly without even reading the input video. For example, Gemini-1.5-Pro can achieve over 50\% accuracy given a random frame from a long video on Video-MME. We also observe that increasing the number of frames does not necessarily lead to improvement on existing benchmarks, which is counterintuitive. As a result, the validity and robustness of current LVU benchmarks are undermined, impeding a faithful assessment of LMMs' long-video understanding capability. To tackle this problem, we propose VideoEval-Pro, a realistic LVU benchmark containing questions with open-ended short-answer, which truly require understanding the entire video. VideoEval-Pro assesses both segment-level and full-video understanding through perception and reasoning tasks. By evaluating 21 proprietary and open-source video LMMs, we conclude the following findings: (1) video LMMs show drastic performance ($>$25\%) drops on open-ended questions compared with MCQs; (2) surprisingly, higher MCQ scores do not lead to higher open-ended scores on VideoEval-Pro; (3) compared to other MCQ benchmarks, VideoEval-Pro benefits more from increasing the number of input frames. Our results show that VideoEval-Pro offers a more realistic and reliable measure of long video understanding, providing a clearer view of progress in this domain.

