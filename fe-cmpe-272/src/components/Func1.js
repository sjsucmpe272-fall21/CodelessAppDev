import React, { useState } from "react";

export default function Func1() {
  // ===========Declare useState===========
  const [desc, setDesc] = useState();
  const [result, setResult] = useState(
    <div className="text-center">initial result</div>
  );
  // ===========Variables===========
  //update this variable from the result set
  let result_textarea_value = "Result code";
  // ===========Commit to Github Button===========
  const submitGithub = (event) => {
    event.preventDefault();
    alert(`Committing result -  ${result_textarea_value}`);
  };
  // ===========Handle Submit Button===========
  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Submitting Name ${desc}`);
    result_textarea_value = "result for description as:" + desc;
    setDesc("");
    setResult(
      <div className="row mt-3">
        <div className="col-md-6 mx-auto">
          <div className="form-group">
            <label htmlFor="functionality1">Description</label>
            <textarea
              className="form-control rounded-0"
              rows="8"
              readOnly={true}
              value={result_textarea_value}
            />
          </div>
          <div className="col text-center">
            <button
              onClick={submitGithub}
              type="submit"
              className="btn btn-primary"
            >
              Commit to Github
            </button>
          </div>
        </div>
      </div>
    );
  };
  // ===========return()===========
  return (
    <div>
      <div className="container">
        <div className="row mb-3">
          <div className="col-md-6 mx-auto">
            <h2 className="h2 text-center mb-3 mt-3">Functionality 1</h2>
            <div className="form-group">
              <label htmlFor="functionality1">Description</label>
              <textarea
                value={desc}
                className="form-control rounded-0"
                onChange={(event) => setDesc(event.target.value)}
                rows="10"
              />
            </div>
            <div className="col text-center">
              <button
                onClick={handleSubmit}
                type="submit"
                className="btn btn-primary"
              >
                Submit
              </button>
            </div>
          </div>
        </div>
        {result}
      </div>
    </div>
  );
}
