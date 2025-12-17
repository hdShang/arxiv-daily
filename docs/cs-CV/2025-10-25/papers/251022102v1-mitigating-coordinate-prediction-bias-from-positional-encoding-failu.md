---
layout: default
title: Mitigating Coordinate Prediction Bias from Positional Encoding Failures
---

# Mitigating Coordinate Prediction Bias from Positional Encoding Failures

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22102" target="_blank" class="toolbar-btn">arXiv: 2510.22102v1</a>
    <a href="https://arxiv.org/pdf/2510.22102.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22102v1" 
            onclick="toggleFavorite(this, '2510.22102v1', 'Mitigating Coordinate Prediction Bias from Positional Encoding Failures')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xingjian Tao, Yiwei Wang, Yujun Cai, Yihong Luo, Jing Tang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-25

---

## 💡 一句话要点

**针对MLLM坐标预测偏差，提出Vision-PE Shuffle Guidance方法提升定位精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `坐标预测` `位置编码` `偏差校正` `视觉语言任务`

## 📋 核心要点

1. MLLM在视觉语言任务中表现出色，但高分辨率输入导致位置编码减弱，坐标预测精度下降。
2. 提出Vision-PE Shuffle Guidance (VPSG)，通过扰动位置编码来估计偏差，并进行校正。
3. 在ScreenSpot-Pro数据集上，VPSG显著提升了坐标预测的准确性，验证了其有效性。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在视觉-语言任务（如VQA和文档理解）中表现出色，但精确的坐标预测仍然具有挑战性。高分辨率输入会产生长token序列，削弱位置编码，并在坐标输出中引入方向偏差，从而加剧了这一难题。本文通过分析MLLM在视觉位置编码(VPE)被故意扰乱（通过洗牌）时的行为来研究这种现象。分析表明，这种扰动会诱导可预测的、非随机的坐标偏差，而不是随机误差，这表明当空间定位信号退化时，模型依赖于内部位置先验。关键的是，在自然高分辨率数据集中观察到类似的方向误差模式，表明位置编码失败是大规模精确坐标预测的关键瓶颈。为了解决这个问题，本文提出了一种无需训练的测试时方法Vision-PE Shuffle Guidance (VPSG)，该方法利用这些偏差的方向性进行校正。VPSG运行带有洗牌VPE的辅助解码以隔离位置非条件倾向，然后将其用作负证据来指导数字预测，同时通过轻量级有限状态机保持坐标格式。在ScreenSpot-Pro上的实验证明了可靠的改进，突出了位置编码鲁棒性是MLLM中空间推理的关键因素。

## 🔬 方法详解

**问题定义**：多模态大语言模型在处理高分辨率图像时，由于视觉位置编码(VPE)的token序列过长，导致位置信息丢失或减弱，从而引起坐标预测的偏差。现有的方法在高分辨率场景下，无法准确地进行空间定位，尤其是在需要精确定位坐标的任务中，性能会显著下降。

**核心思路**：论文的核心思路是利用VPE扰动（洗牌）来揭示模型固有的位置偏差。通过观察在VPE被打乱的情况下，模型预测坐标的倾向性，可以推断出模型在缺乏准确位置信息时所依赖的内部位置先验。然后，利用这些偏差信息作为负证据，来指导模型的坐标预测，从而减少偏差的影响。

**技术框架**：VPSG (Vision-PE Shuffle Guidance) 是一种测试时方法，不需要额外的训练。其主要流程包括：1) 使用原始VPE进行一次坐标预测；2) 对VPE进行洗牌，进行辅助解码，得到位置非条件倾向；3) 将洗牌VPE的预测结果作为负证据，指导原始VPE的预测结果，从而校正坐标偏差；4) 使用轻量级的有限状态机(FSM)来保证输出的坐标格式正确。

**关键创新**：VPSG的关键创新在于利用VPE洗牌来估计和校正坐标预测中的偏差。与传统的增加数据或修改模型结构的方法不同，VPSG是一种无需训练的测试时方法，可以直接应用于现有的MLLM。通过分析VPE扰动后的预测结果，可以有效地揭示模型的位置偏差，并利用这些偏差信息来提高坐标预测的准确性。

**关键设计**：VPSG的关键设计包括：1) VPE洗牌策略，用于生成位置扰动；2) 辅助解码过程，用于估计位置非条件倾向；3) 偏差校正机制，利用洗牌VPE的预测结果作为负证据，指导原始VPE的预测结果；4) 有限状态机(FSM)，用于保证输出的坐标格式正确。具体的参数设置和损失函数没有明确说明，但强调了FSM的轻量级设计，以避免引入额外的计算负担。

## 📊 实验亮点

实验结果表明，VPSG在ScreenSpot-Pro数据集上取得了显著的改进。通过利用洗牌VPE进行偏差校正，VPSG能够有效地减少坐标预测的误差，提高了定位的准确性。具体的性能数据和提升幅度在论文中有所展示，证明了VPSG在解决MLLM坐标预测偏差问题上的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要精确坐标预测的视觉-语言任务，如文档理解、屏幕内容定位、目标检测和视觉问答。通过提高MLLM的坐标预测精度，可以提升这些应用的用户体验和性能，例如在文档中准确定位关键信息，或在屏幕上精确定位用户感兴趣的元素。未来，该方法有望扩展到其他空间推理任务，并促进更智能的人机交互。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) excel at vision-language tasks such as VQA and document understanding, yet precise coordinate prediction remains challenging. High-resolution inputs exacerbate this difficulty by producing long token sequences that weaken positional encodings and introduce directional biases in coordinate outputs. We investigate this phenomenon by analyzing how MLLMs behave when visual positional encodings (VPEs) are deliberately perturbed through shuffling. Our analysis reveals that such perturbations induce predictable, non-random coordinate biases rather than random errors, suggesting that models rely on internal positional priors when spatial grounding signals are degraded. Crucially, we observe similar directional error patterns in natural high-resolution datasets, indicating that positional encoding failures are a key bottleneck for accurate coordinate prediction at scale. To address this issue, we propose Vision-PE Shuffle Guidance (VPSG), a training-free test-time method that leverages the directional nature of these biases for correction. VPSG runs auxiliary decoding with shuffled VPEs to isolate position-unconditioned tendencies, then uses this as negative evidence to guide digit prediction while preserving coordinate format through a lightweight finite-state machine. Experiments on ScreenSpot-Pro demonstrate reliable improvements, highlighting positional encoding robustness as a critical factor for spatial reasoning in MLLMs.

