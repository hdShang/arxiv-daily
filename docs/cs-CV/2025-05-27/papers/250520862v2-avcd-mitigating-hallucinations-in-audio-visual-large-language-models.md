---
layout: default
title: AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding
---

# AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20862" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20862v2</a>
  <a href="https://arxiv.org/pdf/2505.20862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20862v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20862v2', 'AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaeyoung Jung, Youngjoon Jang, Joon Son Chung

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-09-30)

**🔗 代码/项目**: [GITHUB](https://github.com/kaistmm/AVCD)

---

## 💡 一句话要点

**提出AVCD以解决音视频大语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `音视频处理` `对比解码` `幻觉抑制` `自适应解码` `注意力机制` `模型鲁棒性`

## 📋 核心要点

1. 现有的多模态大语言模型在处理音频、视频和文本时，常常会产生幻觉现象，影响模型的可靠性。
2. 本文提出音视频对比解码（AVCD），通过动态识别模态并应用注意力掩蔽，来抑制模态引起的幻觉现象。
3. 在AVHBench数据集上，AVCD在VideoLLaMA2和video-SALMONN模型上分别提高了2%和7%的准确率，展现出良好的鲁棒性和泛化能力。

## 📝 摘要（中文）

幻觉现象仍然是多模态大语言模型（MLLMs）面临的主要挑战。为此，本文提出了一种新的音视频对比解码（AVCD）框架，旨在建模三模态交互并抑制由模态引起的幻觉。与以往在视觉语言模型（VLMs）中采用固定模态的对比解码方法不同，AVCD利用注意力分布动态识别较不占主导地位的模态，并通过注意力掩蔽生成扰动输出logits。此外，本文还引入了基于熵的自适应解码，以提高效率。实验结果表明，AVCD在多个基准数据集上均优于现有解码方法，尤其在AVHBench数据集上，VideoLLaMA2的准确率提高了2%，而video-SALMONN的准确率提高了7%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型（AV-LLMs）中的幻觉现象，现有的对比解码方法在处理音频、视频和文本的复杂交互时效果不佳，导致幻觉频发。

**核心思路**：AVCD框架通过动态识别模态的主导性，利用注意力机制进行模态掩蔽，从而生成更准确的输出logits，减少幻觉的产生。

**技术框架**：AVCD的整体架构包括三个主要模块：模态识别模块、对比解码模块和自适应解码模块。模态识别模块通过注意力分布识别主导模态，对比解码模块生成扰动logits，自适应解码模块根据模型信心选择解码步骤。

**关键创新**：AVCD的创新之处在于其动态模态识别和注意力掩蔽机制，与传统的固定模态对比解码方法相比，能够更有效地应对多模态交互中的幻觉问题。

**关键设计**：在设计中，AVCD采用了熵引导的自适应解码策略，能够根据模型对预测的信心动态调整解码过程，从而提高解码效率和准确性。具体的损失函数和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在AVHBench数据集上，AVCD显著提高了VideoLLaMA2的准确率2%和video-SALMONN的准确率7%，展示了其在多模态解码中的优越性和强大的鲁棒性，超越了现有的解码方法。

## 🎯 应用场景

AVCD框架具有广泛的应用潜力，尤其在需要处理音频、视频和文本的多模态任务中，如视频理解、自动字幕生成和多模态搜索等领域。其有效抑制幻觉现象的能力，将提升相关应用的可靠性和用户体验，推动多模态人工智能的发展。

## 📄 摘要（原文）

> Hallucination remains a major challenge in multimodal large language models (MLLMs). To address this, various contrastive decoding (CD) methods have been proposed that contrasts original logits with hallucinated logits generated from perturbed inputs. While CD has shown promise in vision-language models (VLMs), it is not well-suited for AV-LLMs, where hallucinations often emerge from both unimodal and cross-modal combinations involving audio, video, and language. These intricate interactions call for a more adaptive and modality-aware decoding strategy. In this paper, we propose Audio-Visual Contrastive Decoding (AVCD)-a novel, training-free decoding framework designed to model trimodal interactions and suppress modality-induced hallucinations in AV-LLMs. Unlike previous CD methods in VLMs that corrupt a fixed modality, AVCD leverages attention distributions to dynamically identify less dominant modalities and applies attentive masking to generate perturbed output logits. To support CD in a trimodal setting, we also reformulate the original CD framework to jointly handle audio, visual, and textual inputs. Finally, to improve efficiency, we introduce entropy-guided adaptive decoding, which selectively skips unnecessary decoding steps based on the model's confidence in its predictions. Extensive experiments demonstrate that AVCD consistently outperforms existing decoding methods. Especially, on the AVHBench dataset, it improves accuracy by 2% for VideoLLaMA2 and 7% for video-SALMONN, demonstrating strong robustness and generalizability. Our code is available at https://github.com/kaistmm/AVCD.

